import pytest

from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.add_new_pharmacy import AddNewPharmacy
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.errors.duplicated_error import DuplicatedError


def test_must_create_new_pharmacy():
    repository = PharmacyRepository()
    new_pharmacy = Pharmacy(name="Pharmacy")

    use_case = AddNewPharmacy(pharmacy_repository=repository)
    use_case.execute(new_pharmacy=new_pharmacy)

    assert 1 == len(repository.pharmacies)


def test_duplicate_pharmacy():
    repository = PharmacyRepository()
    new_pharmacy = Pharmacy(name="Pharmacy")

    use_case = AddNewPharmacy(pharmacy_repository=repository)
    use_case.execute(new_pharmacy=new_pharmacy)

    with pytest.raises(DuplicatedError):
        use_case.execute(new_pharmacy=new_pharmacy)