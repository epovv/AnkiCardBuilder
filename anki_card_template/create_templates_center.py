from typing import Optional

from requests.models import Response

from anki_card_template.message_templates.yandex_message_template import \
    JsonYandexMessageTemplate
from extensions.user_data_transfer_object import UserDataTransferObject
from settings.settings import Settings


class CreateTemplateCenter:
    """
    Class to chose creating templates system
    """
    def __init__(self, settings: Settings):
        self.settings = settings

    def yandex_make_template(self, response: Response, user_data: UserDataTransferObject) -> Optional[dict]:
        """
        Make template for Anki
        :param response: Response from api
        :param user_data: user given data
        :return: Data for Anki
        """
        if self.settings.method == 'JSON':
            template = JsonYandexMessageTemplate(self.settings.user_action).make_template(response, user_data)
        else:
            template = None
        return template
