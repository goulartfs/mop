import pytest
from typing import List

from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.patient.list_patients import ListPatients
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_list_patients():
    pharmacy = Pharmacy("Pharmacy")
    pharmacy.patients.append(Patient("Patient"))

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListPatients(pharmacy_repository=repository)
    patients = use_case.execute(pharmacy_id=pharmacy.id)
    assert 1 == len(patients)


def test_must_return_empty_list():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListPatients(pharmacy_repository=repository)
    patients = use_case.execute(pharmacy_id=pharmacy.id)
    assert 0 == len(patients)


def test_must_raise_exception_when_pharmacy_not_found():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    list_patients_use_case = ListPatients(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFoundUseCaseException):
        list_patients_use_case.execute(pharmacy_id='not-found')
