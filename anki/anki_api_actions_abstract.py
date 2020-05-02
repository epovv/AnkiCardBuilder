from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from anki.anki_sender import AnkiSender

if TYPE_CHECKING:
    from anki.anki_interact import AnkiApiCenter


class AnkiApiAbstract(ABC):
    """
    Class to process Anki API actions
    """
    def __init__(self, anki_center: 'AnkiApiCenter', sender: 'AnkiSender'):
        self.anki_center = anki_center
        self.sender = sender

    @abstractmethod
    def choice_method(self, user_action: str, template: dict = None) -> dict:
        """
        Select method by user_action
        :param user_action: Action from user
        :param template: template to send
        :return: response from Anki
        """
        pass
