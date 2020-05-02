import json

from requests import post

from extensions.exceptions.anki_sender_exceptions import (
    MissingErrorFieldException, MissingResultFieldException,
    WrongNumberOfFieldsException)
from extensions.usefull_functions import convert_content_loads


class AnkiSender:
    """
    Class to send request to Anki server
    """
    def __init__(self, anki_host: str):
        self.anki_host = anki_host

    def request(self, action: str, params) -> dict:
        """
        Make request to Anki server
        :param action: Anki action
        :param params: params to send
        :return: response dict
        """
        json_data = self.__data_to_send(action, params)
        response = post(self.anki_host, data=json_data)
        response_result = convert_content_loads(response.content)
        self.__response_validate(response_result)
        return response_result

    @staticmethod
    def __data_to_send(action: str, params) -> bytes:
        """
        Make data to send
        :param action: Anki action
        :param params: params to send
        :return: json data to send
        """
        data = {'action': action, 'version': 6, 'params': params}
        json_data = json.dumps(data).encode('utf-8')
        return json_data

    @staticmethod
    def __response_validate(response: dict):
        """
        Validate response from Anki
        :param response: dict from Anki
        """
        if len(response) != 2:
            raise WrongNumberOfFieldsException()
        if 'error' not in response:
            raise MissingErrorFieldException()
        if 'result' not in response:
            raise MissingResultFieldException()
