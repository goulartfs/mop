from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.entities.errors.duplicated_patient_error import DuplicatedPatientError
from domain.use_cases.patient.errors.duplicated_error import DuplicatedError
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound

class AddNewPatient:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, new_patient: Patient, pharmacy: Pharmacy) -> None:
        stored_farmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)

        if not stored_farmacy:
            raise PharmacyNotFound

        try:
            stored_farmacy.add_patient(new_patient)
        except DuplicatedPatientError:
            raise DuplicatedError

        self.pharmacy_repository.update(pharmacy_id=pharmacy.id, updated_pharmacy=stored_farmacy)