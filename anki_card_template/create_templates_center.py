from typing import Optional

from requests.models import Response

from anki_card_template.message_templates.yandex_message_template import \
    JsonYandexMessageTemplate
from settings.settings import Settings


class CreateTemplateCenter:
    """
    Class to chose creating templates system
    """
    def __init__(self, settings: Settings):
        self.settings = settings

    def yandex_make_template(self, response: Response) -> Optional[dict]:
        """
        Make template for Anki
        :param response: Response from api
        :return: Data for Anki
        """
        if self.settings.method == 'JSON':
            template = JsonYandexMessageTemplate(self.settings.user_action).make_template(response)
        else:
            template = None
        return template
