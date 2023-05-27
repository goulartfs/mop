import hashlib
from typing import List

from domain.entities.errors.duplicated_medicine_error import DuplicatedMedicineError
from domain.entities.errors.duplicated_patient_error import DuplicatedPatientError
from domain.entities.errors.medicine_not_found_error import MedicineNotFoundError
from domain.entities.errors.patient_not_found_error import PatientNotFoundError
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

    def insert_medicine(self, new_medicine: Medicine) -> None:
        for medicine in self.medicines:
            if medicine.id == new_medicine.id:
                raise DuplicatedMedicineError
        self.medicines.append(new_medicine)

    def insert_patient(self, new_patient: Patient) -> None:
        for patient in self.patients:
            if patient.id == new_patient.id:
                raise DuplicatedPatientError
        self.patients.append(new_patient)

    def update_patient(self, patient_id: str, updated_patient: Patient) -> None:
        for idx, patient in enumerate(self.patients):
            if patient_id == patient.id:
                self.patients[idx] = updated_patient
                return None

        raise PatientNotFoundError

    def delete_patient(self, patient_id: str) -> None:
        for idx, patient in enumerate(self.patients):
            if patient.id == patient_id:
                print(f"Removing Patient: #{patient_id} - {patient.name}")
                self.patients.pop(idx)
                return None

        raise PatientNotFoundError

    def delete_medicine(self, medicine_id: str) -> None:
        for idx, medicine in enumerate(self.medicines):
            if medicine.id == medicine_id:
                print(f"Removing Medicine: #{medicine_id} - {medicine.name}, Dosage: {medicine.dosage}")
                self.medicines.pop(idx)
                return None

        raise MedicineNotFoundError

    def update_medicine(self, medicine_id, updated_medicine: Medicine):
        for idx, medicine in enumerate(self.medicines):
            if medicine.id == medicine_id:
                self.medicines[idx] = updated_medicine
                return None

        raise MedicineNotFoundError
