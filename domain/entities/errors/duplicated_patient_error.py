class DuplicatedPatientError(Exception):
    def __init__(self):
        message = "Duplicated patient entry"
        super().__init__(message)