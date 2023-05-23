from app.services.medicine_service import MedicineService
from app.entities.medicine import Medicine
from infrastructure.memory.repositories.medicine_repository import MedicineRepository

def test_must_return_empty_list():
    service = MedicineService(
        repository=MedicineRepository()
    )
    
    medicines = []
    medicines = service.list()

    assert len(medicines) == 0

def test_must_add_new_medicine():
    service = MedicineService(
        repository=MedicineRepository()
    )
    
    medicines = []
    medicines = service.list()
    assert len(medicines) == 0

    service.add(Medicine("Medicine 1", "1mg"))

    medicines = []
    medicines = service.list()
    assert len(medicines) == 1

def test_must_remove_a_given_medicine():
    service = MedicineService(
        repository=MedicineRepository()
    )

    medicine1 = Medicine("Medicine 1", "1mg")
    medicine2 = Medicine("Medicine 2", "2mg")
    medicine3 = Medicine("Medicine 3", "2mg")

    expected_list = [medicine1, medicine3]
    
    service.add(medicine1)
    service.add(medicine2)
    service.add(medicine3)

    assert len(service.list()) == 3

    service.remove(medicine2)
    list = service.list()

    assert len(list) == 2
    assert expected_list == list
