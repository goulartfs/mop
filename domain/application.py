from typing import List

from domain.entities.medicine import Medicine
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.entities.prescription import Prescription


class Application:
    def add_new_medicine(self, pharmacy: Pharmacy, medicine: Medicine) -> None:
        raise NotImplementedError()

    def remove_medicine(self, pharmacy: Pharmacy, medicine: Medicine) -> None:
        raise NotImplementedError()

    def get_medicine_list(self, pharmacy: Pharmacy) -> List[Medicine]:
        raise NotImplementedError()

    def register_patient(self, pharmacy: Pharmacy, patient: Patient) -> None:
        raise NotImplementedError()

    def remove_patience(self, pharmacy: Pharmacy, patient: Patient) -> None:
        raise NotImplementedError()

    def get_patient_list(self, pharmacy: Pharmacy) -> List[Patient]:
        raise NotImplementedError()

    def get_patient_prescription(self, pharmacy: Pharmacy, Patient: Patient) -> Prescription:
        raise NotImplementedError()
