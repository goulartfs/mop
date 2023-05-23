from typing import List
from domain.entities.patient import Patient
from domain.repositories.repository import Repository


class PatientRepository(Repository):
    def add(self, patient: Patient) -> None:
        raise NotImplementedError()
    
    def remove(self, patient: Patient) -> None:
        raise NotImplementedError()
    
    def list(self) -> List[Patient]:
        raise NotImplementedError()