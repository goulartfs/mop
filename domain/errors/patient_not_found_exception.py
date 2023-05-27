class PatientNotFoundException(Exception):
    def __init__(self) -> None:
        message = 'Patient not found.'
        super().__init__(message)
