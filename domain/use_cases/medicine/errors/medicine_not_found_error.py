class MedicineNotFoundError(Exception):
    def __init__(self):
        message = 'Medicine not found in pharmacy.'
        super().__init__(message)
