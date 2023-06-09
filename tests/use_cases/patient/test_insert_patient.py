import pytest

from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.patient.errors.duplicated_error import DuplicatedError
from domain.use_cases.patient.insert_patient import InsertPatient
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from domain.use_cases.pharmacy.insert_pharmacy import InsertPharmacy
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_insert_new_medicine_to_existent_pharmacy():
    repository = PharmacyRepository()

    new_pharmacy = Pharmacy(name="New Pharmacy")
    new_patient = Patient(name="Patient")

    create_pharmacy = InsertPharmacy(pharmacy_repository=repository)
    create_pharmacy.execute(new_pharmacy=new_pharmacy)

    use_case = InsertPatient(pharmacy_repository=repository)
    use_case.execute(new_patient=new_patient, pharmacy=new_pharmacy)

    assert 1 == len(repository.pharmacies[0].patients)


def test_duplicate_patient():
    repository = PharmacyRepository()

    new_pharmacy = Pharmacy(name="New Pharmacy")
    new_patient = Patient(name="Patient")

    create_pharmacy = InsertPharmacy(pharmacy_repository=repository)
    create_pharmacy.execute(new_pharmacy=new_pharmacy)

    use_case = InsertPatient(pharmacy_repository=repository)
    use_case.execute(new_patient=new_patient, pharmacy=new_pharmacy)

    with pytest.raises(DuplicatedError):
        use_case.execute(new_patient=new_patient, pharmacy=new_pharmacy)


def test_pharmacy_not_found():
    repository = PharmacyRepository()

    pharmacy = Pharmacy(name="Pharmacy not found")
    new_patient = Patient(name="Patient")

    use_case = InsertPatient(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFoundUseCaseException):
        use_case.execute(new_patient=new_patient, pharmacy=pharmacy)
