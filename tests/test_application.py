import pytest

from domain.application import Application
from domain.entities.medicine import Medicine
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.errors.pharmacy_not_found_exception \
    import PharmacyNotFoundException
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.use_cases.pharmacy.insert_pharmacy import InsertPharmacy
from infrastructure.memory.repositories.pharmacy_repository \
    import PharmacyRepository as InMemoryPharmacy
from domain.use_cases.pharmacy.errors.duplicated_error import DuplicatedError


def __get_application(
        pharmacy_repository: PharmacyRepository = None) -> Application:
    if pharmacy_repository is None:
        pharmacy_repository = InMemoryPharmacy()

    application = Application(pharmacy_repository=pharmacy_repository)

    return application


def test_must_init_with_pharmacy_list_empty():
    application = __get_application()
    assert 0 == len(application.list_pharmacies())


def test_must_insert_pharmacy():
    application = __get_application()
    application.insert_pharmacy(new_pharmacy=Pharmacy("Pharmacy"))
    assert 1 == len(application.list_pharmacies())


def test_must_init_with_medicines_list_empty():
    pharmacy = Pharmacy("Pharmacy")
    application = __get_application()
    application.insert_pharmacy(new_pharmacy=pharmacy)
    assert len(application.list_medicines(pharmacy)) == 0


def test_must_init_with_patient_list_empty():
    pharmacy = Pharmacy("Pharmacy")
    application = __get_application()
    application.insert_pharmacy(new_pharmacy=pharmacy)
    assert len(application.list_patients(pharmacy)) == 0


def test_must_insert_medicine():
    pharmacy = Pharmacy("Pharmacy")
    new_medicine = Medicine("Medicine 1", "1mg")

    application = __get_application()
    application.insert_pharmacy(new_pharmacy=pharmacy)
    application.insert_medicine(pharmacy=pharmacy, new_medicine=new_medicine)
    medicine_list = application.list_medicines(pharmacy)

    assert len(medicine_list) == 1
    assert new_medicine == medicine_list[0]


def test_must_insert_patient():
    pharmacy = Pharmacy("Pharmacy")
    new_patient = Patient(name="Patient")

    application = __get_application()
    application.insert_pharmacy(new_pharmacy=pharmacy)
    application.insert_patient(pharmacy=pharmacy, new_patient=new_patient)
    patient_list = application.list_patients(pharmacy=pharmacy)

    assert len(patient_list) == 1
    assert new_patient == patient_list[0]


def test_must_raise_exception_when_pharmacy_not_found():
    pharmacy = Pharmacy("Pharmacy")
    application = __get_application()

    with pytest.raises(PharmacyNotFoundException):
        application.list_patients(pharmacy=pharmacy)
    with pytest.raises(PharmacyNotFoundException):
        application.list_medicines(pharmacy=pharmacy)
    with pytest.raises(PharmacyNotFoundException):
        application.insert_patient(
            pharmacy=pharmacy, new_patient=Patient('Patient'))
    with pytest.raises(PharmacyNotFoundException):
        application.insert_medicine(
            pharmacy=pharmacy, new_medicine=Medicine("Medicine", "1mg"))
    with pytest.raises(PharmacyNotFoundException):
        application.update_medicine(
            pharmacy_id=pharmacy.id, medicine_id='not-found',
            updated_medicine=Medicine("Medicine", "1mg"))
    with pytest.raises(PharmacyNotFoundException):
        application.delete_patient(
            pharmacy=pharmacy, patient=Patient('Patient'))
    with pytest.raises(PharmacyNotFoundException):
        application.delete_medicine(
            pharmacy=pharmacy, medicine=Medicine("Medicine", "1mg"))


def test_must_register_patient():
    pharmacy = Pharmacy("Pharmacy1")
    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = InsertPharmacy(pharmacy_repository=pharmacy_repository)
    create_pharmacy.execute(new_pharmacy=pharmacy)
    application = __get_application(pharmacy_repository=pharmacy_repository)

    patient = Patient("John Doe")
    application.insert_patient(pharmacy, patient)
    patient_list = application.list_patients(pharmacy)
    assert 1 == len(patient_list)
    assert patient == patient_list[0]


def test_must_raise_exception_when_inserting_pharmacy_id_equals_zero():
    pharmacy1 = Pharmacy("Pharmacy1")
    pharmacy1.id = 0
    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = InsertPharmacy(pharmacy_repository=pharmacy_repository)

    with pytest.raises(Exception):
        create_pharmacy.execute(new_pharmacy=pharmacy1)


def test_must_raise_exception_when_pharmacy_id_is_invalid():
    pharmacy1 = Pharmacy("Pharmacy1")
    pharmacy1.id = None

    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = InsertPharmacy(pharmacy_repository=pharmacy_repository)

    with pytest.raises(Exception):
        create_pharmacy.execute(new_pharmacy=pharmacy1)


def test_must_raise_exception_when_pharmacy_inserted_already_exists():
    pharmacy1 = Pharmacy("Pharmacy1")
    pharmacy1.id = 1
    pharmacy2 = Pharmacy("Pharmacy2")
    pharmacy2.id = 1

    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = InsertPharmacy(pharmacy_repository=pharmacy_repository)
    create_pharmacy.execute(new_pharmacy=pharmacy1)

    with pytest.raises(DuplicatedError):
        create_pharmacy.execute(new_pharmacy=pharmacy2)


def test_should_affect_given_pharmacy():
    pharmacy1 = Pharmacy("Pharmacy1")
    pharmacy1.id = 1
    pharmacy2 = Pharmacy("Pharmacy2")
    pharmacy2.id = 2
    new_medicine1 = Medicine("Medicine1", "1mg")
    new_medicine2 = Medicine("Medicine2", "10mg")

    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = InsertPharmacy(pharmacy_repository=pharmacy_repository)
    create_pharmacy.execute(new_pharmacy=pharmacy1)
    create_pharmacy.execute(new_pharmacy=pharmacy2)

    application = __get_application(pharmacy_repository=pharmacy_repository)

    application.insert_medicine(pharmacy1, new_medicine1)
    application.insert_medicine(pharmacy2, new_medicine1)
    application.insert_medicine(pharmacy2, new_medicine2)

    application.list_medicines(pharmacy1)
    assert 1 == len(application.list_medicines(pharmacy1))
    assert 2 == len(application.list_medicines(pharmacy2))
