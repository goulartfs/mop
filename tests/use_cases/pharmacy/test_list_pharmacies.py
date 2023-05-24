from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.list_pharmacies import ListPharmacies
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository


def test_must_return_empty_list():
    repository = PharmacyRepository()
    use_case = ListPharmacies(pharmacy_repository=repository)
    assert 0 == len(use_case.execute())


def test_must_list_pharmacies():
    pharmacy = Pharmacy("Pharmacy")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = ListPharmacies(pharmacy_repository=repository)
    assert 1 == len(use_case.execute())
