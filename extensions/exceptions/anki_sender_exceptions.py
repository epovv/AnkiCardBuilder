class WrongNumberOfFieldsException(Exception):

    def __init__(self):
        error_message = 'Response has an unexpected number of fields'
        super(WrongNumberOfFieldsException, self).__init__(error_message)


class MissingErrorFieldException(Exception):

    def __init__(self):
        error_message = 'Response is missing required error field'
        super(MissingErrorFieldException, self).__init__(error_message)


class MissingResultFieldException(Exception):

    def __init__(self):
        error_message = 'Response is missing required result field'
        super(MissingResultFieldException, self).__init__(error_message)
