class PharmacyNotFoundException(Exception):
    def __init__(self) -> None:
        message = "Pharmacy not found."
        super().__init__(message)
