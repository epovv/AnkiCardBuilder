class GetUrlException(Exception):
    """
    Exception while url not exist for defined method
    """
    def __init__(self):
        error_message = 'Url not exist for defined method'
        super(GetUrlException, self).__init__(error_message)


class ResponseValidateException(Exception):
    """
    Response have bad http code for continue
    """
    def __init__(self, status_code, response_text):
        error_message = f'Bad response, status: {status_code}, text: {response_text}'
        super(ResponseValidateException, self).__init__(error_message)
