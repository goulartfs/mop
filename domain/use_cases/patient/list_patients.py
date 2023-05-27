from typing import List
from domain.entities.patient import Patient
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException


class ListPatients:
    def __init__(self, pharmacy_repository: PharmacyRepository) -> None:
        self.pharmacy_repository = pharmacy_repository
    def execute(self, pharmacy_id:str) -> List[Patient]:
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)
        
        if not stored_pharmacy:
            raise PharmacyNotFoundUseCaseException
        
        return stored_pharmacy.patients