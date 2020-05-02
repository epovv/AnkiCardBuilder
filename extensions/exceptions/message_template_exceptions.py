class ResponseEmptyException(Exception):
    """
    Exception while url not exist for defined method
    """
    def __init__(self, response_content):
        error_message = f'Response content is empty: {response_content}, perhaps bad client request'
        super(ResponseEmptyException, self).__init__(error_message)
