import pytest

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.medicine.delete_medicine import DeleteMedicine
from domain.use_cases.medicine.errors.medicine_not_found_error import MedicineNotFoundError
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_remove_medicine():
    repository = PharmacyRepository()

    medicine = Medicine(name="Medicine", dosage="1mg")
    pharmacy = Pharmacy(
        name="New Pharmacy",
        medicines=[
            medicine
        ]
    )

    repository.pharmacies.append(pharmacy)

    use_case = DeleteMedicine(pharmacy_repository=repository)
    use_case.execute(medicine_id=medicine.id, pharmacy_id=pharmacy.id)

    assert 0 == len(repository.pharmacies[0].medicines)


def test_must_raise_exception_when_pharmacy_not_found():
    repository = PharmacyRepository()

    medicine = Medicine(name="Medicine", dosage="1mg")
    pharmacy = Pharmacy(
        name="New Pharmacy",
        medicines=[
            medicine
        ]
    )

    use_case = DeleteMedicine(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFound):
        use_case.execute(medicine_id=medicine.id, pharmacy_id='not-found')


def test_must_raise_exception_when_medicine_not_found():
    repository = PharmacyRepository()

    medicine = Medicine(name="Medicine", dosage="1mg")
    pharmacy = Pharmacy(
        name="New Pharmacy",
        medicines=[
            medicine
        ]
    )

    repository.pharmacies.append(pharmacy)

    use_case = DeleteMedicine(pharmacy_repository=repository)

    with pytest.raises(MedicineNotFoundError):
        use_case.execute(medicine_id="not-found", pharmacy_id=pharmacy.id)
