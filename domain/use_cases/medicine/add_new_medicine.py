from domain.entities.errors.duplicated_medicine_error import DuplicatedMedicineError
from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.medicine.errors.duplicated_error import DuplicatedError
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound


class AddNewMedicine:
    """
    Caso de uso: Adicionar novo remédio

    História do usuário: Como administrador, gostaria de adicionar um novo medicamento a uma determinada farmácia
    """

    def __init__(self,
                 pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, new_medicine: Medicine, pharmacy: Pharmacy):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)

        if not stored_pharmacy:
            raise PharmacyNotFound

        try:
            stored_pharmacy.add_medicine(new_medicine=new_medicine)
        except DuplicatedMedicineError:
            raise DuplicatedError
        self.pharmacy_repository.update(pharmacy_id=pharmacy.id, updated_pharmacy=stored_pharmacy)
