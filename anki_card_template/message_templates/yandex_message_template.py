from typing import Callable

from requests.models import Response

from anki_card_template.message_templates.abstract_message_template import \
    AbstractMessageTemplate
from extensions.exceptions.message_template_exceptions import \
    ResponseEmptyException
from extensions.usefull_functions import convert_content_loads

MethodToCreateTemplate = Callable[[dict], dict]


class JsonYandexMessageTemplate(AbstractMessageTemplate):
    """
    Class for creating template with Yandex response
    """

    def make_template(self, response: Response) -> dict:
        """
        Make template for Anki if response method as JSON
        :param response: Response from api
        :return: Data for Anki
        """
        response_dict = convert_content_loads(response.content).get('def', None)
        self.__validate_by_content(response_dict)
        template_creator = self.chose_template_create_method_by_user_action()
        template = template_creator(response_dict)

        return template

    def chose_template_create_method_by_user_action(self) -> MethodToCreateTemplate:
        if self.user_action == 'create_one_note':
            template_creator = self.template_for_one_note
        else:
            template_creator = None
        return template_creator

    def template_for_one_note(self, response_dict: dict) -> dict:
        """
        template for one note
        :param response_dict: response from Yandex API
        :return: dict to send
        """
        template = {}
        template['front'] = response_dict[0]['text']
        back = ''
        for pos in response_dict:
            translate = ''

            for tr in pos['tr']:
                translate += f"{tr['text']} "

                syn = tr.get('syn')
                if syn is not None:
                    syn_string = ', '.join([word['text'] for word in syn])
                    translate += f"&nbsp;(Synonyms: {syn_string})"
                translate += '<br>&nbsp;&nbsp;&nbsp;&nbsp;'

            back += f"Part of speech: {pos['pos']}<br>" \
                    f"Translate:<br>&nbsp;&nbsp;&nbsp;&nbsp;{translate}<br>"

        template['back'] = back
        return template

    @staticmethod
    def __validate_by_content(response_content: dict):
        """
        If content is empty
        :param response_content: content from response
        """
        if response_content is None or response_content == []:
            raise ResponseEmptyException(response_content)
