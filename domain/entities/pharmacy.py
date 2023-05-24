import hashlib
from typing import List

from domain.entities.errors.duplicated_medicine_error import DuplicatedMedicineError
from domain.entities.errors.duplicated_patient_error import DuplicatedPatientError
from domain.entities.medicine import Medicine
from domain.entities.patient import Patient


class Pharmacy:
    def __init__(self,
                 name: str,
                 medicines: List[Medicine] = None,
                 patients: List[Patient] = None):
        if medicines is None:
            medicines = []
        if patients is None:
            patients = []

        self.name = name
        self.medicines = medicines
        self.patients = patients

    def __eq__(self, other) -> bool:
        if isinstance(other, Pharmacy):
            return self.id == other.id
        return False

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

    def add_patient(self, new_patient: Patient) -> None:
        for patient in self.patients:
            if patient.id == new_patient.id:
                raise DuplicatedPatientError
        self.patients.append(new_patient)

    def remove_medicine(self, medicine_id: str) -> None:
        for idx, medicine in enumerate(self.medicines):
            if medicine.id == medicine_id:
                self.medicines.pop(idx)
                print(f"Removing Medicine: #{medicine_id} - {medicine.name}, Dosage: {medicine.dosage}")
