from typing import Callable, Optional

from requests.models import Response

from anki_card_template.message_templates.abstract_message_template import \
    AbstractMessageTemplate
from extensions.exceptions.message_template_exceptions import \
    ResponseEmptyException
from extensions.usefull_functions import convert_content_loads
from extensions.user_data_transfer_object import UserDataTransferObject

MethodToCreateTemplate = Callable[[dict, UserDataTransferObject], dict]


class JsonYandexMessageTemplate(AbstractMessageTemplate):
    """
    Class for creating template with Yandex response
    """

    def make_template(self, response: Response, user_data: UserDataTransferObject) -> dict:
        """
        Make template for Anki if response method as JSON
        :param response: Response from api
        :param user_data: user given data
        :return: Data for Anki
        """
        response_dict = convert_content_loads(response.content).get('def', None)
        self.__validate_by_content(response_dict)
        template_creator = self.chose_template_create_method_by_user_action()
        template = template_creator(response_dict, user_data)

        return template

    def chose_template_create_method_by_user_action(self) -> Optional[MethodToCreateTemplate]:
        if self.user_action == 'create_one_note':
            template_creator = self.template_for_one_note
        else:
            template_creator = None
        return template_creator

    def template_for_one_note(self, response_dict: dict, user_data: UserDataTransferObject) -> dict:
        """
        template for one note
        :param response_dict: response from Yandex API
        :param user_data: user given data
        :return: dict to send
        """
        template = {}
        template['front'] = f'{user_data.text_to_translate}'

        back = f'User example: {user_data.text_example}<br><br>'
        for pos in response_dict:
            translate = ''

            for tr in pos['tr']:
                translate += f"- {tr['text']} "
                translate = self.add_syn_and_example(tr, translate)
            part_of_speech = pos.get('pos', 'None part of speech')
            back += f"Part of speech: {part_of_speech}<br>" \
                    f"Translate:<br>&nbsp;&nbsp;&nbsp;&nbsp;{translate}" \
                    f"<br>----------------------------<br>"

        template['back'] = back
        return template

    @staticmethod
    def add_syn_and_example(tr: dict, translate: str) -> str:
        syn = tr.get('syn')
        example = tr.get('ex')
        if syn is not None:
            syn_string = ', '.join([word['text'] for word in syn])
            translate += f"&nbsp;(Synonyms: {syn_string})"

        if example is not None:
            example_string = '<br>'.join(
                ['&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                 + word['text'] + ' - ' + word['tr'][0]['text'] for word in example]
            )
            translate += f"<br>{example_string}<br>"

        translate += '<br>&nbsp;&nbsp;&nbsp;&nbsp;'
        return translate

    @staticmethod
    def __validate_by_content(response_content: dict):
        """
        If content is empty
        :param response_content: content from response
        """
        if response_content is None or response_content == []:
            raise ResponseEmptyException(response_content)
