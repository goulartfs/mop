from typing import List

from domain.entities.medicine import Medicine


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.medicines: List[Medicine] = []  # List of Medicine objects

    def add_medicine(self, medicine: Medicine) -> None:
        self.medicines.append(medicine)

    def remove_medicine(self, medicine: Medicine) -> None:
        print(f"Removing Medicine: {medicine.name}, Dosage: {medicine.dosage}")
        self.medicines.remove(medicine)
