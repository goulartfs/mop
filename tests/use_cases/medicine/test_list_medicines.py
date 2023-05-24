from typing import List

from domain.entities.medicine import Medicine
from domain.entities.pharmacy import Pharmacy
from domain.use_cases.medicine.list_medicines import ListMedicines
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_list_medicines():
    pharmacy = Pharmacy("Pharmacy")
    pharmacy.medicines.append(Medicine("Medicine", "1mg"))

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListMedicines(pharmacy_repository=repository)
    medicines = use_case.execute(pharmacy_id=pharmacy.id)
    assert 1 == len(medicines)
