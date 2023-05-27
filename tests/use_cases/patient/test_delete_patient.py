import pytest

from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.patient.delete_patient import DeletePatient
from domain.use_cases.patient.errors.patient_not_found_use_case_exception import PatientNotFoundUseCaseException
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_remove_patient():
    patient = Patient(name="Patient")
    pharmacy = Pharmacy(
        name="Pharmacy",
        patients=[
            patient
        ]
    )

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = DeletePatient(pharmacy_repository=repository)
    use_case.execute(patient_id=patient.id, pharmacy_id=pharmacy.id)

    assert 0 == len(repository.pharmacies[0].patients)


def test_must_raise_exception_when_pharmacy_not_found():
    patient = Patient(name="Patient")
    pharmacy = Pharmacy(
        name="Pharmacy",
        patients=[
            patient
        ]
    )

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = DeletePatient(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFoundUseCaseException):
        use_case.execute(patient_id=patient.id, pharmacy_id='not-found')


def test_must_raise_exception_when_medicine_not_found():
    patient = Patient(name="Patient")
    pharmacy = Pharmacy(
        name="Pharmacy",
        patients=[
            patient
        ]
    )

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = DeletePatient(pharmacy_repository=repository)

    with pytest.raises(PatientNotFoundUseCaseException):
        use_case.execute(patient_id="not-found", pharmacy_id=pharmacy.id)
