from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.errors.duplicated_error import DuplicatedError


class InsertPharmacy:
    def __init__(self, pharmacy_repository: PharmacyRepository) -> None:
        self.repository = pharmacy_repository

    def execute(self, new_pharmacy: Pharmacy) -> None:
        if new_pharmacy.id == 0:
            raise Exception("pharmacy_id cannot be equals zero")
        
        stored_pharmacy = self.repository.find_by_id(new_pharmacy.id)

        if stored_pharmacy:
            raise DuplicatedError

        self.repository.insert(new_pharmacy)
