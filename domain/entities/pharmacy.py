from typing import List
import hashlib
from domain.entities.medicine import Medicine
from domain.entities.errors.duplicated_medicine_error import DuplicatedMedicineError


class Pharmacy:
    def __init__(self, name: str, medicines: List[Medicine] = None):
        if medicines is None:
            medicines = []

        self.name = name
        self.medicines = medicines

    @property
    def id(self) -> str:
        md5_hash = hashlib.md5()
        md5_hash.update(self.name.encode('utf-8'))
        return md5_hash.hexdigest()

    def add_medicine(self, new_medicine: Medicine) -> None:
        for medicine in self.medicines:
            if medicine.id == new_medicine.id:
                raise DuplicatedMedicineError
        self.medicines.append(new_medicine)

    def remove_medicine(self, medicine: Medicine) -> None:
        print(f"Removing Medicine: {medicine.name}, Dosage: {medicine.dosage}")
        self.medicines.remove(medicine)
