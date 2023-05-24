import pytest
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.update_pharmacy import UpdatePharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_update_pharmacy():
    pharmacy = Pharmacy(name="Pharmacy")
    updated_pharmacy = Pharmacy(name="PharmacyUpdate")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = UpdatePharmacy(pharmacy_repository=repository)
    use_case.execute(pharmacy_id=pharmacy.id, updated_pharmacy=updated_pharmacy)

    assert updated_pharmacy == repository.pharmacies[0]


def test_must_raise_exception_when_pharmacy_not_found():
    pharmacy = Pharmacy(name="Pharmacy")
    updated_pharmacy = Pharmacy(name="PharmacyUpdate")

    repository = PharmacyRepository()

    use_case = UpdatePharmacy(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFound):
        use_case.execute(pharmacy_id=pharmacy.id, updated_pharmacy=updated_pharmacy)
