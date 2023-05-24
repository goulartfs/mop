from app.application import Application
from app.entities.medicine import Medicine
from app.entities.patient import Patient
from app.entities.pharmacy import Pharmacy
from app.services.medicine_service import MedicineService
from app.services.patient_service import PatientService
from infrastructure.memory.repositories.medicine_repository import MedicineRepository
from infrastructure.memory.repositories.patient_repository import PatientRepository

pharmacy = Pharmacy("Filipe")


def __get_application(medicine_service: MedicineService = None,
                      patient_service: PatientService = None) -> Application:
    if medicine_service == None:
        medicine_service = MedicineService(
            repository=MedicineRepository()
        )

    if patient_service == None:
        patient_service = PatientService(
            repository=PatientRepository()
        )

    application = Application(
        medicine_service=medicine_service,
        patient_service=patient_service
    )

    return application


def test_must_init_with_medicines_list_empty():
    application = __get_application()
    assert len(application.get_medicine_list(pharmacy)) == 0


def test_must_init_with_patient_list_empty():
    application = __get_application()
    assert len(application.get_patient_list(pharmacy)) == 0


def test_must_add_new_medicine():
    application = __get_application()

    new_medicine = Medicine("Medicine 1", "1mg")
    application.add_new_medicine(pharmacy, new_medicine)

    list = application.get_medicine_list(pharmacy)
    assert len(list) == 1
    assert new_medicine == list[0]


def test_must_register_patient():
    application = __get_application()

    patient = Patient("John Doe")
    application.register_patient(pharmacy, patient)
    patient_list = application.get_patient_list(pharmacy)
    assert len(patient_list) == 1
    assert patient == patient_list[0]
