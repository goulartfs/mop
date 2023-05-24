import pytest

from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.patient.update_patient import UpdatePatient
from domain.use_cases.medicine.errors.patient_not_found_use_case_exception import PatientNotFoundUseCaseException
from domain.use_cases.pharmacy.errors.pharmacy_not_found_use_case_exception import PharmacyNotFoundUseCaseException
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_update_patient():
    repository = PharmacyRepository()

    patient = Patient(name="Patient")
    updated_patient = Patient(name="PatientUpdated")

    pharmacy = Pharmacy(
        name="New Pharmacy",
        patients=[
            patient
        ]
    )

    repository.pharmacies.append(pharmacy)

    use_case = UpdatePatient(pharmacy_repository=repository)
    use_case.execute(patient_id=patient.id, pharmacy_id=pharmacy.id, updated_patient=updated_patient)

    assert updated_patient == repository.pharmacies[0].patients[0]


def test_must_raise_exception_when_pharmacy_not_found():
    repository = PharmacyRepository()

    patient = Patient(name="Patient")
    updated_patient = Patient(name="PatientUpdated")

    use_case = UpdatePatient(pharmacy_repository=repository)

    with pytest.raises(PharmacyNotFoundUseCaseException):
        use_case.execute(patient_id=patient.id, pharmacy_id='not-found', updated_patient=updated_patient)


def test_must_raise_exception_when_patient_not_found():
    repository = PharmacyRepository()

    patient = Patient(name="Patient")
    updated_patient = Patient(name="PatientUpdated")

    pharmacy = Pharmacy(
        name="Pharmacy",
        patients=[
            patient
        ]
    )

    repository.pharmacies.append(pharmacy)
    use_case = UpdatePatient(pharmacy_repository=repository)

    with pytest.raises(PatientNotFoundUseCaseException):
        use_case.execute(patient_id='not-found', pharmacy_id=pharmacy.id, updated_patient=updated_patient)
