from typing import List
from domain.entities.patient import Patient


class PatientService:
    def list(self) -> List[Patient]:
        raise NotImplementedError()
    
    def add(self, patient: Patient) -> None:
        raise NotImplementedError()
    
    def remove(self, patient: Patient) -> None:
        raise NotImplementedError()
