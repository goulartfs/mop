from domain.entities.pharmacy import Pharmacy
from domain.use_cases.pharmacy.update_pharmacy import UpdatePharmacy
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository

# atualizar farmacia
#   - atualiza farmacia
#   - atualiza lista de pacientes
# atualizar farmacia
#   - farmacia nao existe


def test_must_update_pharmacy():
    pharmacy = Pharmacy(name="Pharmacy")
    updated_pharmacy = Pharmacy(name="PharmacyUpdate")

    repository = PharmacyRepository()
    repository.pharmacies.append(pharmacy)

    use_case = UpdatePharmacy(pharmacy_repository=repository)
    use_case.execute(pharmacy_id=pharmacy.id, updated_pharmacy=updated_pharmacy)

    assert updated_pharmacy == repository.pharmacies[0]
