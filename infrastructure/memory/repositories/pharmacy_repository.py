import copy
from typing import List

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository as Repository


class PharmacyRepository(Repository):
    def __init__(self):
        self.pharmacies: List[Pharmacy] = []

    def insert(self, pharmacy: Pharmacy):
        self.pharmacies.append(pharmacy)

    def remove(self, pharmacy_id: str):
        for idx, pharmacy in enumerate(self.pharmacies):
            if pharmacy_id == pharmacy.id:
                self.pharmacies.pop(idx)

    def list(self) -> List[Pharmacy]:
        return self.pharmacies

    def update(self, pharmacy_id: str, updated_pharmacy: Pharmacy):
        for idx, pharmacy in enumerate(self.pharmacies):
            if pharmacy_id == pharmacy.id:
                self.pharmacies[idx].name = updated_pharmacy.name
                self.pharmacies[idx].medicines = updated_pharmacy.medicines
                self.pharmacies[idx].patients = updated_pharmacy.patients

    def find_by_id(self, pharmacy_id: str) -> Pharmacy | None:
        for pharmacy in self.pharmacies:
            if pharmacy_id == pharmacy.id:
                return copy.deepcopy(pharmacy)

        return None

    def add_medicine(self, pharmacy: Pharmacy, medicine: Medicine):
        stored_pharmacy = self.find_by_id(pharmacy_id=pharmacy.id)
        stored_pharmacy.add_medicine(medicine)
