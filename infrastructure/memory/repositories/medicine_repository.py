from typing import List

from domain.entities.medicine import Medicine
from domain.repositories.medicine_repository import MedicineRepository as Repository


class MedicineRepository(Repository):
    def __init__(self) -> None:
        self.medicines = []

    def insert(self, medicine: Medicine) -> None:
        self.medicines.append(medicine)

    def remove(self, medicine: Medicine) -> None:
        self.medicines.remove(medicine)

    def list(self) -> List[Medicine]:
        return self.medicines
