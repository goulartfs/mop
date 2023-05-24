from domain.entities.medicine import Medicine
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.entities.errors.medicine_not_found_error import MedicineNotFoundError
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from domain.use_cases.medicine.errors.medicine_not_found_use_case_exception import \
    MedicineNotFoundUseCaseException as MedicineNotFoundUseCaseError


class UpdateMedicine:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, medicine_id: str, pharmacy_id: str, updated_medicine: Medicine):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)

        if not stored_pharmacy:
            raise PharmacyNotFoundUseCaseException

        try:
            stored_pharmacy.update_medicine(medicine_id=medicine_id, updated_medicine=updated_medicine)
        except MedicineNotFoundError:
            raise MedicineNotFoundUseCaseError

        self.pharmacy_repository.update(pharmacy_id=stored_pharmacy.id, updated_pharmacy=stored_pharmacy)