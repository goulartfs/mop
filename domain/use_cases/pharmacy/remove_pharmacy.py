from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from domain.repositories.pharmacy_repository import PharmacyRepository


class RemovePharmacy:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, pharmacy_id: str):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)
        if not stored_pharmacy:
            raise PharmacyNotFound
        self.pharmacy_repository.remove(pharmacy_id=stored_pharmacy.id)
