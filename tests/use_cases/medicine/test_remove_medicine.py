import pytest

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.medicine.remove_medicine import RemoveMedicine
from domain.use_cases.medicine.errors.duplicated_error import DuplicatedError
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

    use_case = RemoveMedicine(pharmacy_repository=repository)
    use_case.execute(medicine_id=medicine.id, pharmacy_id=pharmacy.id)

    assert 0 == len(repository.pharmacies[0].medicines)
