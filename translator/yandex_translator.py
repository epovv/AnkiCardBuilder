from requests import Response, post

from extensions.exceptions.translator_exceptions import (
    GetUrlException, ResponseValidateException)
from translator.abstract_translator import AbstractTranslator


class YandexTranslator(AbstractTranslator):
    """
    Class to interactions with Yandex remote API
    """
    def __init__(self, settings):
        super(YandexTranslator, self).__init__(settings=settings)
        self.data_creator = YandexDataCreator(settings)

    def get_response(self, text_to_translate) -> Response:
        """
        Get response from remote API
        :param text_to_translate: text to send at API
        :return: response from Yandex
        """
        data = self.data_creator.data_to_send(text_to_translate)
        url = self.data_creator.get_url_to_send()
        response = post(url=url, data=data)
        self.response_validate(response)
        return response

    @staticmethod
    def response_validate(response: Response):
        """
        If bad status code for continue
        :param response: response from Yandex
        """
        bad_status_code = [400, 401, 402, 403, 413, 501]
        if response.status_code in bad_status_code:
            raise ResponseValidateException(response.status_code, response.text)


class YandexDataCreator:

    def __init__(self, settings):
        self.settings = settings

    def data_to_send(self, text_to_translate) -> dict:
        """
        Create data to send at API
        :param text_to_translate: text to send at API
        :return: dict with data
        """
        data = {
            'key': self.settings.api_key,
            'text': text_to_translate,
            'lang': self.get_language_to_send(),
            'ui': 'en'
        }
        return data

    def get_url_to_send(self) -> str:
        """
        Get url to send depends from METHOD
        :return: api url to send
        """
        urls = {
            'JSON':
                f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='
                f'{self.settings.api_key}&lang=en-ru&text=time',
            'XML':
                f'https://dictionary.yandex.net/api/v1/dicservice/lookup?key='
                f'{self.settings.api_key}&lang=en-ru&text=time',
        }
        url_to_send = urls.get(self.settings.method, None)
        if url_to_send is None:
            raise GetUrlException()

        return url_to_send

    def get_language_to_send(self) -> str:
        """
        Get language for translate
        :return: language from-to
        """
        language = f'{self.settings.lang_from}-{self.settings.lang_to}'
        return language
