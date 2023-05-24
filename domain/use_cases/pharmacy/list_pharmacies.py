from typing import List
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository


class ListPharmacies:
    def __init__(self, pharmacy_repository: PharmacyRepository) -> None:
        self.pharmacy_repository = pharmacy_repository

    def execute(self) -> List[Pharmacy]:
        return self.pharmacy_repository.list()
