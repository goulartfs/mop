from domain.entities.errors.duplicated_patient_error import DuplicatedPatientError
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.patient.errors.duplicated_error import DuplicatedError
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException


class InsertPatient:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.pharmacy_repository = pharmacy_repository

    def execute(self, new_patient: Patient, pharmacy: Pharmacy) -> None:
        stored_farmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy.id)

        if not stored_farmacy:
            raise PharmacyNotFoundUseCaseException

        try:
            stored_farmacy.insert_patient(new_patient)
        except DuplicatedPatientError:
            raise DuplicatedError

        self.pharmacy_repository.update(pharmacy_id=pharmacy.id, updated_pharmacy=stored_farmacy)
