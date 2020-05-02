from abc import ABC, abstractmethod

from requests import Response

from settings.settings import Settings


class AbstractTranslator(ABC):
    """
    Abstract class for translate API logic
    """
    def __init__(self, settings: Settings):
        self.settings = settings

    @abstractmethod
    def get_response(self, text_to_translate: str) -> Response:
        """
        Get response from remote API
        :return: requests.Response object
        """
        pass
