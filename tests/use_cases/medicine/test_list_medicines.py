import pytest
from typing import List

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.medicine.list_medicines import ListMedicines
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_list_medicines():
    pharmacy = Pharmacy("Pharmacy")
    pharmacy.medicines.append(Medicine("Medicine", "1mg"))

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListMedicines(pharmacy_repository=repository)
    medicines = use_case.execute(pharmacy_id=pharmacy.id)
    assert 1 == len(medicines)


def test_must_return_empty_list():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListMedicines(pharmacy_repository=repository)
    medicines = use_case.execute(pharmacy_id=pharmacy.id)
    assert 0 == len(medicines)


def test_must_raise_exception_when_pharmacy_not_found():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListMedicines(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFoundUseCaseException):
        use_case.execute(pharmacy_id='not-found')
