import pytest
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.remove_pharmacy import RemovePharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_remove_pharmacy():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = RemovePharmacy(pharmacy_repository=repository)
    use_case.execute(pharmacy_id=pharmacy.id)

    assert 0 == len(repository.pharmacies)


def test_must_raise_exception_when_pharmacy_not_found():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()

    use_case = RemovePharmacy(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFound):
        use_case.execute(pharmacy_id=pharmacy.id)
