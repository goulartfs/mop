from typing import List

from domain.services.patient_service import PatientService as Service

from domain.entities.patient import Patient
from domain.repositories.patient_repository import PatientRepository


class PatientService(Service):
    def __init__(self, repository: PatientRepository) -> None:
        self.repository = repository

    def add(self, patient: Patient) -> None:
        self.repository.insert(patient)

    def list(self) -> List[Patient]:
        return self.repository.list()

    def remove(self, patient: Patient) -> None:
        self.repository.remove(patient)
