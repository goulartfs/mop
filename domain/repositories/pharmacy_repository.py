from typing import List

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.repositories.repository import Repository


class PharmacyRepository(Repository):
    def add(self, pharmacy: Pharmacy):
        raise NotImplementedError()

    def remove(self, pharmacy_id: str):
        raise NotImplementedError()

    def update(self, pharmacy_id: str, updated_pharmacy: Pharmacy):
        raise NotImplementedError()

    def list(self) -> List[Pharmacy]:
        raise NotImplementedError()

    def find_by_id(self, pharmacy_id: str) -> Pharmacy:
        raise NotImplementedError()

    def add_medicine(self, pharmacy: Pharmacy, medicine: Medicine):
        raise NotImplementedError()
