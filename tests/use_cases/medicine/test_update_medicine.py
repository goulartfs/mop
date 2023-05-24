import pytest

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.medicine.update_medicine import UpdateMedicine
from domain.use_cases.medicine.errors.medicine_not_found_error import MedicineNotFoundError
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_update_medicine():
    repository = PharmacyRepository()

    medicine = Medicine(name="Medicine", dosage="1mg")
    updated_medicine = Medicine(name="MedicineUpdated", dosage="2mg")
    pharmacy = Pharmacy(
        name="New Pharmacy",
        medicines=[
            medicine
        ]
    )

    repository.pharmacies.append(pharmacy)

    use_case = UpdateMedicine(pharmacy_repository=repository)
    use_case.execute(medicine_id=medicine.id, pharmacy_id=pharmacy.id, updated_medicine=updated_medicine)

    assert updated_medicine == repository.pharmacies[0].medicines[0]