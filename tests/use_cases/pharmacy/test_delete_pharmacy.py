import pytest

from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from domain.use_cases.pharmacy.delete_pharmacy import DeletePharmacy
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_delete_pharmacy():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = DeletePharmacy(pharmacy_repository=repository)
    use_case.execute(pharmacy_id=pharmacy.id)

    assert 0 == len(repository.pharmacies)


def test_must_raise_exception_when_pharmacy_not_found():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()

    use_case = DeletePharmacy(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFoundUseCaseException):
        use_case.execute(pharmacy_id=pharmacy.id)
