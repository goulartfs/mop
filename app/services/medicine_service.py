from typing import List

from domain.entities.medicine import Medicine
from domain.repositories.medicine_repository import MedicineRepository
from domain.services.medicine_service import MedicineService as Service


class MedicineService(Service):
    def __init__(self, repository: MedicineRepository) -> None:
        super().__init__()
        self.medicine_repository = repository

    def list(self) -> List[Medicine]:
        return self.medicine_repository.list()

    def add(self, medicine: Medicine) -> None:
        self.medicine_repository.add(medicine)

    def remove(self, medicine: Medicine) -> None:
        self.medicine_repository.remove(medicine)
