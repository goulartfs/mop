from typing import List
from domain.application import Application as App
from domain.entities.medicine import Medicine
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.services.medicine_service import MedicineService
from domain.services.patient_service import PatientService

class Application(App):
    def __init__(self,
                 medicine_service: MedicineService,
                 patient_service: PatientService) -> None:
        self.medicine_service = medicine_service
        self.patient_service = patient_service

    def get_medicine_list(self, pharmacy: Pharmacy) -> List[Medicine]:
        return self.medicine_service.list()
    
    def get_patient_list(self, pharmacy: Pharmacy) -> List[Patient]:
        return self.patient_service.list()
    
    def register_patient(self, pharmacy: Pharmacy, patient: Patient) -> None:
        self.patient_service.add(patient)
    
    def add_new_medicine(self, pharmacy: Pharmacy, medicine: Medicine) -> None:
        self.medicine_service.add(medicine)