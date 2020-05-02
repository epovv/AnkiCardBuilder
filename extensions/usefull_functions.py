import json

from extensions.exceptions.another_exceptions import ConvertDataToJsonException


def convert_content_loads(content: bytes) -> dict:
    """
    Validation of the structure received from the response
    :param content: content from response
    :return data: dict with content
    """
    try:
        data = json.loads(content.decode('utf-8'))
    except json.JSONDecodeError:
        raise ConvertDataToJsonException()
    return data
