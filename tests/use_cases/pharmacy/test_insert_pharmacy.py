import pytest

from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.errors.duplicated_error import DuplicatedError
from domain.use_cases.pharmacy.insert_pharmacy import InsertPharmacy
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_insert_new_pharmacy():
    repository = PharmacyRepository()
    new_pharmacy = Pharmacy(name="Pharmacy")

    use_case = InsertPharmacy(pharmacy_repository=repository)
    use_case.execute(new_pharmacy=new_pharmacy)

    assert 1 == len(repository.pharmacies)


def test_duplicate_pharmacy():
    repository = PharmacyRepository()
    new_pharmacy = Pharmacy(name="Pharmacy")

    use_case = InsertPharmacy(pharmacy_repository=repository)
    use_case.execute(new_pharmacy=new_pharmacy)

    with pytest.raises(DuplicatedError):
        use_case.execute(new_pharmacy=new_pharmacy)
