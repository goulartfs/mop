import pytest

from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.patient.add_new_patient import AddNewPatient
from domain.use_cases.patient.errors.duplicated_error import DuplicatedError
from domain.use_cases.pharmacy.add_new_pharmacy import AddNewPharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_add_new_medicine_to_existent_pharmacy():
    repository = PharmacyRepository()

    new_pharmacy = Pharmacy(name="New Pharmacy")
    new_patient = Patient(name="Patient")

    create_pharmacy = AddNewPharmacy(pharmacy_repository=repository)
    create_pharmacy.execute(new_pharmacy=new_pharmacy)

    use_case = AddNewPatient(pharmacy_repository=repository)
    use_case.execute(new_patient=new_patient, pharmacy=new_pharmacy)

    assert 1 == len(repository.pharmacies[0].patients)


def test_duplicate_patient():
    repository = PharmacyRepository()

    new_pharmacy = Pharmacy(name="New Pharmacy")
    new_patient = Patient(name="Patient")

    create_pharmacy = AddNewPharmacy(pharmacy_repository=repository)
    create_pharmacy.execute(new_pharmacy=new_pharmacy)

    use_case = AddNewPatient(pharmacy_repository=repository)
    use_case.execute(new_patient=new_patient, pharmacy=new_pharmacy)

    with pytest.raises(DuplicatedError):
        use_case.execute(new_patient=new_patient, pharmacy=new_pharmacy)


def test_pharmacy_not_found():
    repository = PharmacyRepository()

    pharmacy = Pharmacy(name="Pharmacy not found")
    new_patient = Patient(name="Patient")

    use_case = AddNewPatient(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFound):
        use_case.execute(new_patient=new_patient, pharmacy=pharmacy)
