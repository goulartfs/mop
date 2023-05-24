from domain.entities.errors.medicine_not_found_error import MedicineNotFoundError
from domain.use_cases.medicine.errors.medicine_not_found_error import \
    MedicineNotFoundError as MedicineNotFoundUseCaseException
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from domain.repositories.pharmacy_repository import PharmacyRepository


class DeleteMedicine:

    def __init__(self,
                 pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, medicine_id: str, pharmacy_id: str):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)

        if not stored_pharmacy:
            raise PharmacyNotFoundUseCaseException

        try:
            stored_pharmacy.delete_medicine(medicine_id=medicine_id)
        except MedicineNotFoundError:
            raise MedicineNotFoundUseCaseException
        self.pharmacy_repository.update(pharmacy_id=stored_pharmacy.id, updated_pharmacy=stored_pharmacy)
