import pytest

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.medicine.add_new_medicine import AddNewMedicine
from domain.use_cases.medicine.errors.duplicated_error import DuplicatedError
from domain.use_cases.pharmacy.add_new_pharmacy import AddNewPharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_add_new_medicine_to_existent_pharmacy():
    repository = PharmacyRepository()

    new_pharmacy = Pharmacy(name="New Pharmacy")
    new_medicine = Medicine(name="Medicine", dosage="1mg")

    create_pharmacy = AddNewPharmacy(pharmacy_repository=repository)
    create_pharmacy.execute(new_pharmacy=new_pharmacy)

    use_case = AddNewMedicine(pharmacy_repository=repository)
    use_case.execute(new_medicine=new_medicine, pharmacy=new_pharmacy)

    assert 1 == len(repository.pharmacies[0].medicines)


def test_duplicate_medicine():
    repository = PharmacyRepository()

    new_pharmacy = Pharmacy(name="New Pharmacy")
    new_medicine = Medicine(name="Medicine", dosage="1mg")

    create_pharmacy = AddNewPharmacy(pharmacy_repository=repository)
    create_pharmacy.execute(new_pharmacy=new_pharmacy)

    use_case = AddNewMedicine(pharmacy_repository=repository)
    use_case.execute(new_medicine=new_medicine, pharmacy=new_pharmacy)

    with pytest.raises(DuplicatedError):
        use_case.execute(new_medicine=new_medicine, pharmacy=new_pharmacy)


def test_pharmacy_not_found():
    repository = PharmacyRepository()

    pharmacy = Pharmacy(name="Pharmacy not found")
    new_medicine = Medicine(name="Medicine", dosage="1mg")

    use_case = AddNewMedicine(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFound):
        use_case.execute(new_medicine=new_medicine, pharmacy=pharmacy)
