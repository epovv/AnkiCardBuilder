from anki.anki_interact import AnkiApiCenter
from anki_card_template.create_templates_center import CreateTemplateCenter
from extensions.user_data_transfer_object import UserDataTransferObject
from settings.settings import Settings
from translator.yandex_translator import YandexTranslator


class MainDispatcher:

    def __init__(self, setting: Settings):
        self.settings = setting
        self.anki_api_center = AnkiApiCenter(settings=settings)
        self.template_center = CreateTemplateCenter(settings=settings)

    def dispatch(self, user_data: UserDataTransferObject):
        """
        Main point
        :param user_data: user given data
        """
        template = self.create_template(user_data)
        response_from_anki = self.anki_api_center.anki_action(user_action=settings.user_action, template=template)

        self.response_message(response_from_anki)

    def create_template(self, user_data: UserDataTransferObject) -> dict:
        """
        Chose template creator by usage api
        :param user_data: user given data
        :return: template dict
        """
        if self.settings.usage_api == 'YANDEX':
            response_from_api = YandexTranslator(self.settings).get_response(user_data)
            template = self.template_center.yandex_make_template(response_from_api, user_data)
        else:
            template = None
        return template

    @staticmethod
    def response_message(response_from_anki):
        """
        Write message to console according to response from Anki server
        :param response_from_anki: response from Anki server
        """
        if response_from_anki is not None:
            result = response_from_anki.get('result')
            error = response_from_anki.get('error')

            if result is not None:
                print(f'Card {result} was created')
            else:
                print(f'An error occurred: {error}')
        else:
            print('Bad response')


if __name__ == '__main__':

    settings = Settings()
    settings.get_external_settings()

    while True:
        try:
            text_to_translate = input('Input word to translate: ')
            text_example = input('Input example(not necessary): ')

            user_data = UserDataTransferObject()
            user_data.text_to_translate = text_to_translate
            user_data.text_example = text_example

            user_action = 'create_one_note'

            settings.user_action = user_action
            MainDispatcher(settings).dispatch(user_data)
        except Exception as e:
            print(e)
            pass
