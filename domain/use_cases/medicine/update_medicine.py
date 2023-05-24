from domain.entities.medicine import Medicine
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound


class UpdateMedicine:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, medicine_id: str, pharmacy_id: str, updated_medicine: Medicine):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)

        if not stored_pharmacy:
            raise PharmacyNotFound

        for idx, medicine in enumerate(stored_pharmacy.medicines):
            if medicine.id == medicine_id:
                stored_pharmacy.medicines[idx] = updated_medicine

        self.pharmacy_repository.update(pharmacy_id=stored_pharmacy.id, updated_pharmacy=stored_pharmacy)