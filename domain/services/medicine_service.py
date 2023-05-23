from typing import List
from domain.entities.medicine import Medicine
from domain.repositories.repository import Repository


class MedicineService:
    def repository() -> Repository:
        raise NotImplementedError()
    
    def list(self) -> List[Medicine]:
        """
        Lists pharmacy's medicine list
        """
        raise NotImplementedError()
    
    def add(self, medicine: Medicine) -> None:
        """
        Add new medicine to pharmacy's medicine storage
        """
        raise NotImplementedError()
    
    def remove(self, medicine: Medicine) -> None:
        """
        Removes a medicine from pharmacy's medicine storage
        """
        raise NotImplementedError()