from typing import List
from domain.entities.medicine import Medicine
from domain.repositories.repository import Repository

class MedicineRepository(Repository):
    def add(self, medicine: Medicine) -> None:
        raise NotImplementedError()
    
    def remove(self, medicine: Medicine) -> None:
        raise NotImplementedError()
    
    def list(self) -> List[Medicine]:
        raise NotImplementedError()
        