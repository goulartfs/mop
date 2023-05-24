class DuplicatedError(Exception):
    def __init__(self):
        message = 'Patient already added.'
        super().__init__(message)
