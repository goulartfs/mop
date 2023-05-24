from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.errors.duplicated_error import DuplicatedError


class AddNewPharmacy:
    def __init__(self, pharmacy_repository: PharmacyRepository) -> None:
        self.repository = pharmacy_repository

    def execute(self, new_pharmacy: Pharmacy) -> None:
        stored_pharmacy = self.repository.find_by_id(new_pharmacy.id)

        if stored_pharmacy:
            raise DuplicatedError

        self.repository.add(new_pharmacy)
