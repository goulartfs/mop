from domain.entities.errors.patient_not_found_error import PatientNotFoundError
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.patient.errors.patient_not_found_use_case_exception import PatientNotFoundUseCaseException
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException


class DeletePatient:
    def __init__(self, pharmacy_repository: PharmacyRepository) -> None:
        self.pharmacy_repository = pharmacy_repository

    def execute(self, patient_id: str, pharmacy_id: str):
        stored_pharmacy = self.pharmacy_repository.find_by_id(pharmacy_id=pharmacy_id)

        if not stored_pharmacy:
            raise PharmacyNotFoundUseCaseException

        try:
            stored_pharmacy.delete_patient(patient_id=patient_id)
        except PatientNotFoundError:
            raise PatientNotFoundUseCaseException
        self.pharmacy_repository.update(pharmacy_id=stored_pharmacy.id, updated_pharmacy=stored_pharmacy)
