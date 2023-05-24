import pytest
from domain.application import Application
from domain.entities.medicine import Medicine
from domain.entities.patient import Patient
from domain.entities.pharmacy import Pharmacy
from domain.repositories.pharmacy_repository import PharmacyRepository
from domain.repositories.medicine_repository import MedicineRepository
from domain.repositories.patient_repository import PatientRepository
from domain.use_cases.pharmacy.add_new_pharmacy import AddNewPharmacy
from domain.use_cases.pharmacy.errors.pharmacy_not_found_error import PharmacyNotFound
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository as InMemoryPharmacy
from infrastructure.memory.repositories.medicine_repository import MedicineRepository as InMemoryMedicine
from infrastructure.memory.repositories.patient_repository import PatientRepository as InMemoryPatient


def __get_application(pharmacy_repository: PharmacyRepository = None,
                      medicine_repository: MedicineRepository = None,
                      patient_repository: PatientRepository = None) -> Application:
    if pharmacy_repository is None:
        pharmacy_repository = InMemoryPharmacy()

    if medicine_repository is None:
        medicine_repository = InMemoryMedicine()

    if patient_repository is None:
        patient_repository = InMemoryPatient()

    application = Application(
        pharmacy_repository=pharmacy_repository,
        medicine_repository=medicine_repository,
        patient_repository=patient_repository
    )

    return application


def test_must_init_with_medicines_list_empty():
    application = __get_application()
    assert len(application.get_medicine_list(Pharmacy("Filipe"))) == 0


def test_must_init_with_patient_list_empty():
    application = __get_application()
    assert len(application.get_patient_list(Pharmacy("Filipe"))) == 0


def test_must_add_new_medicine():
    pharmacy = Pharmacy("Filipe")
    new_medicine = Medicine("Medicine 1", "1mg")

    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = AddNewPharmacy(pharmacy_repository=pharmacy_repository)
    create_pharmacy.execute(new_pharmacy=pharmacy)

    application = __get_application(pharmacy_repository=pharmacy_repository)
    application.add_new_medicine(pharmacy, new_medicine)
    medicine_list = application.get_medicine_list(pharmacy)

    assert len(medicine_list) == 1
    assert new_medicine == medicine_list[0]


def test_must_raise_exception_when_pharmacy_not_found():
    new_patient = Patient("John Doe")
    application = __get_application()

    with pytest.raises(PharmacyNotFound):
        application.register_patient(Pharmacy("Filipe"), new_patient)


def test_must_register_patient():
    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = AddNewPharmacy(pharmacy_repository=pharmacy_repository)
    create_pharmacy.execute(new_pharmacy=Pharmacy("Pharmacy1"))
    application = __get_application(pharmacy_repository=pharmacy_repository)

    patient = Patient("John Doe")
    application.register_patient(Pharmacy("Pharmacy1"), patient)
    patient_list = application.get_patient_list(Pharmacy("Pharmacy1"))
    assert 1 == len(patient_list)
    assert patient == patient_list[0]


def test_deve_separar_medicamentos_por_farmacia():
    pharmacy1 = Pharmacy("Pharmacy1")
    pharmacy2 = Pharmacy("Pharmacy2")
    new_medicine1 = Medicine("Medicine1", "1mg")
    new_medicine2 = Medicine("Medicine2", "10mg")

    pharmacy_repository = InMemoryPharmacy()
    create_pharmacy = AddNewPharmacy(pharmacy_repository=pharmacy_repository)
    create_pharmacy.execute(new_pharmacy=pharmacy1)
    create_pharmacy.execute(new_pharmacy=pharmacy2)

    application = __get_application(pharmacy_repository=pharmacy_repository)

    application.add_new_medicine(pharmacy1, new_medicine1)
    application.add_new_medicine(pharmacy2, new_medicine1)
    application.add_new_medicine(pharmacy2, new_medicine2)

    application.get_medicine_list(pharmacy1)
    assert 1 == len(application.get_medicine_list(pharmacy1))
    assert 2 == len(application.get_medicine_list(pharmacy2))
