from abc import ABC, abstractmethod
from typing import Callable

from requests.models import Response

from extensions.user_data_transfer_object import UserDataTransferObject


class AbstractMessageTemplate(ABC):
    """
    Class for creating template for Anki card
    """

    def __init__(self, user_action: str):
        self.user_action = user_action

    @abstractmethod
    def make_template(self, response: Response, user_data: UserDataTransferObject) -> dict:
        """
        Make template for Anki if response method as JSON
        :param response: Response from api
        :return: Data for Anki
        """
        pass

    @abstractmethod
    def chose_template_create_method_by_user_action(self) -> Callable[[dict, UserDataTransferObject], dict]:
        """
        Chose method to create template by user action
        :return: callable function to create template
        """
        pass
