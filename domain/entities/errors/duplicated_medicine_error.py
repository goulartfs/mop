class DuplicatedMedicineError(Exception):
    def __init__(self):
        message = "Duplicated message entry"
        super().__init__(message)