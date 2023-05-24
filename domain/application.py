from typing import List

from domain.entities.medicine import Medicine
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.entities.prescription import Prescription
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.repositories.medicine_repository import MedicineRepository
from domain.repositories.patient_repository import PatientRepository
from domain.use_cases.medicine.add_new_medicine import AddNewMedicine
from domain.use_cases.patient.add_new_patient import AddNewPatient


class Application:
    def __init__(self,
                 pharmacy_repository: PharmacyRepository,
                 medicine_repository: MedicineRepository,
                 patient_repository: PatientRepository) -> None:
        self.pharmacy_repository = pharmacy_repository
        self.medicine_repository = medicine_repository
        self.patient_repository = patient_repository

    def add_new_medicine(self, pharmacy: Pharmacy, new_medicine: Medicine) -> None:
        add_medicine = AddNewMedicine(pharmacy_repository=self.pharmacy_repository)
        add_medicine.execute(new_medicine=new_medicine, pharmacy=pharmacy)

    def remove_medicine(self, pharmacy: Pharmacy, medicine: Medicine) -> None:
        raise NotImplementedError()

    def get_medicine_list(self, pharmacy: Pharmacy) -> List[Medicine]:
        pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)
        if not pharmacy:
            return []
        return pharmacy.medicines

    def register_patient(self, pharmacy: Pharmacy, new_patient: Patient) -> None:
        add_patient = AddNewPatient(pharmacy_repository=self.pharmacy_repository)
        add_patient.execute(new_patient=new_patient, pharmacy=pharmacy)

    def remove_patience(self, pharmacy: Pharmacy, patient: Patient) -> None:
        raise NotImplementedError()

    def get_patient_list(self, pharmacy: Pharmacy) -> List[Patient]:
        pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)
        if not pharmacy:
            return []
        return pharmacy.patients

    def get_patient_prescription(self, pharmacy: Pharmacy, patient: Patient) -> Prescription:
        raise NotImplementedError()
