from typing import List

from domain.entities.medicine import Medicine
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException


class ListMedicines:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, pharmacy_id: str) -> List[Medicine]:
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)
        if not stored_pharmacy:
            raise PharmacyNotFoundUseCaseException

        return stored_pharmacy.medicines
