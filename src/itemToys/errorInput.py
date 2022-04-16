class ErrorInput(Exception):

    def __init__(self, message):
        super(ErrorInput, self).__init__(message)
