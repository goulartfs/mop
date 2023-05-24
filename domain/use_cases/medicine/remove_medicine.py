from domain.repositories.pharmacy_repository import PharmacyRepository


class RemoveMedicine:

    def __init__(self,
                 pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, medicine_id: str, pharmacy_id: str):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)
        stored_pharmacy.remove_medicine(medicine_id=medicine_id)
        self.pharmacy_repository.update(pharmacy_id=stored_pharmacy.id, updated_pharmacy=stored_pharmacy)
