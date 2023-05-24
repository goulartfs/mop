class MedicineNotFoundError(Exception):
    def __init__(self):
        message = 'Medicine not found.'
        super().__init__(message)
