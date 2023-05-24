from typing import List

from domain.entities.medicine import Medicine
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.entities.prescription import Prescription
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.medicine.insert_medicine import InsertMedicine
from domain.use_cases.medicine.delete_medicine import DeleteMedicine
from domain.use_cases.patient.insert_patient import InsertPatient
from domain.use_cases.pharmacy.insert_pharmacy import InsertPharmacy
from domain.use_cases.pharmacy.update_pharmacy import UpdatePharmacy
from domain.use_cases.pharmacy.delete_pharmacy import DeletePharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from domain.errors.pharmacy_not_found_exception import PharmacyNotFoundException


class Application:
    def __init__(self,
                 pharmacy_repository: PharmacyRepository) -> None:
        self.pharmacy_repository = pharmacy_repository

    def insert_medicine(self, pharmacy: Pharmacy, new_medicine: Medicine) -> None:
        add_medicine = InsertMedicine(pharmacy_repository=self.pharmacy_repository)
        try:
            add_medicine.execute(new_medicine=new_medicine, pharmacy=pharmacy)
        except PharmacyNotFoundUseCaseException:
            raise PharmacyNotFoundException

    def delete_medicine(self, pharmacy: Pharmacy, medicine: Medicine) -> None:
        delete = DeleteMedicine(pharmacy_repository=self.pharmacy_repository)
        try:
            delete.execute(pharmacy_id=pharmacy.id, medicine_id=medicine.id)
        except PharmacyNotFoundUseCaseException:
            raise PharmacyNotFoundException

    def list_medicines(self, pharmacy: Pharmacy) -> List[Medicine]:
        pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)

        if not pharmacy:
            raise PharmacyNotFoundException

        return pharmacy.medicines

    def insert_patient(self, pharmacy: Pharmacy, new_patient: Patient) -> None:
        add_patient = InsertPatient(pharmacy_repository=self.pharmacy_repository)
        try:
            add_patient.execute(new_patient=new_patient, pharmacy=pharmacy)
        except PharmacyNotFoundUseCaseException:
            raise PharmacyNotFoundException

    def remove_patience(self, pharmacy: Pharmacy, patient: Patient) -> None:
        raise NotImplementedError()

    def list_patients(self, pharmacy: Pharmacy) -> List[Patient]:
        pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)
        if not pharmacy:
            raise PharmacyNotFoundException
        return pharmacy.patients

    def get_patient_prescription(self, pharmacy: Pharmacy, patient: Patient) -> Prescription:
        raise NotImplementedError()

    def list_pharmacies(self) -> List[Pharmacy]:
        return self.pharmacy_repository.list()

    def insert_pharmacy(self, new_pharmacy: Pharmacy):
        insert = InsertPharmacy(pharmacy_repository=self.pharmacy_repository)
        insert.execute(new_pharmacy=new_pharmacy)

    def delete_patient(self, pharmacy: Pharmacy, patient:Patient):
        raise PharmacyNotFoundException


