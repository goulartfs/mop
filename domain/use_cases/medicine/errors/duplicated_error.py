class DuplicatedError(Exception):
    def __init__(self):
        message = 'Medicine already added.'
        super().__init__(message)
