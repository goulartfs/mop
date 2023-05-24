class DuplicatedError(Exception):
    def __init__(self):
        message = 'Pharmacy already created.'
        super().__init__(message)
