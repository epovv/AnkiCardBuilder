class ConvertDataToJsonException(Exception):
    """
    Cant convert data to json
    """
    def __init__(self):
        error_message = 'Data not convert'
        super(ConvertDataToJsonException, self).__init__(error_message)
