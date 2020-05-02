from typing import Type, Union

from anki.anki_api_actions import AnkiApiAddNote, AnkiApiCommonActions
from anki.anki_sender import AnkiSender
from settings.settings import Settings

InteractClass = Union[Type[AnkiApiAddNote], Type[AnkiApiCommonActions], None]


class AnkiApiCenter:
    """
    Class to interact with Anki API
    """
    def __init__(self, settings: Settings):
        self.settings = settings
        self.sender = AnkiSender(anki_host=self.settings.anki_host)

    def anki_action(self, user_action: str, template: dict = None) -> dict:
        """
        Request to Anki server by user action
        :param user_action: Action from user
        :param template: template to request
        :return: response from Anki
        """
        class_to_action = self.chose_class_to_action(user_action)
        response = class_to_action(
            anki_center=self, sender=self.sender
        ).choice_method(user_action=user_action, template=template)

        return response

    def chose_class_to_action(self, user_action: str) -> InteractClass:
        """
        Chose class to action by anki action
        :param user_action: Action from user
        :return: class to action
        """
        anki_action = self.settings.get_anki_action_by_user_action(user_action)

        if anki_action == 'addNote':
            chosen_class_to_action = AnkiApiAddNote
        elif anki_action == 'modelFieldNames':
            chosen_class_to_action = AnkiApiCommonActions
        else:
            chosen_class_to_action = None
        return chosen_class_to_action
