from typing import List
from app.entities.patient import Patient
from domain.repositories.patient_repository import PatientRepository as Repository

class PatientRepository(Repository):
    def __init__(self) -> None:
        self.patients = []

    def add(self, medicine: Patient) -> None:
        self.patients.append(medicine)
    
    def remove(self, patient: Patient) -> None:
        self.patients.remove(patient)
    
    def list(self) -> List[Patient]:
        return self.patients