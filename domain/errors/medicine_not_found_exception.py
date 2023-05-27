class MedicineNotFoundException(Exception):
    def __init__(self) -> None:
        message = 'Medicine not found.'
        super().__init__(message)
