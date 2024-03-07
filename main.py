from app.application import Application
from app.entities.medicine import Medicine
from app.entities.pharmacy import Pharmacy
from app.services.medicine_service import MedicineService
from app.services.patient_service import PatientService
from infrastructure.mysql.repositories.pharmacy_repository import PharmacyRepository, GeradorDeConexao
from infrastructure.memory.repositories.pharmacy_repository import PharmacyRepository as InMemory
from infrastructure.memory.repositories.patient_repository import PatientRepository




def main(*args, **kwargs):
    application = Application(
        pharmacy_repository=PharmacyRepository(conexao=GeradorDeConexao(host="localhost", user="exampleuser", password="examplepassword", database="mop"))
    )

    application_inmemory = Application(
        pharmacy_repository=InMemory()
    )

    pharmacy = Pharmacy("My Own Pharmacy")
    pharmacy.id = 6
    application_inmemory.insert_pharmacy(new_pharmacy=pharmacy)

    application_inmemory.insert_medicine(pharmacy, Medicine("Besilato de anlodipino", "5mg"))
    application_inmemory.insert_medicine(pharmacy, Medicine("Prolopa HBS", "100/25mg"))
    application_inmemory.insert_medicine(pharmacy, Medicine("Prolopa BD", "100/25mg"))
    application_inmemory.insert_medicine(pharmacy, Medicine("Risperidona", "1mg", prescription=True))
    application_inmemory.insert_medicine(pharmacy, Medicine("Sinvastatina", "40mg"))
    application_inmemory.insert_medicine(pharmacy, Medicine("AAS Protect", "100mg"))
    application_inmemory.insert_medicine(pharmacy, Medicine("Cloridrato de metformina", "500mg"))
    application_inmemory.insert_medicine(pharmacy, Medicine("Losartana potássica", "50mg"))

    print(f'Printing Medicine\'s list')
    for medicine in application.list_medicines(pharmacy):
        print(f"- {medicine.name} {medicine.dosage} - {medicine.boxes} caixas")

    print(f'Inmemory Printing Medicine\'s list')
    for medicine in application_inmemory.list_medicines(pharmacy):
        print(f"- {medicine.name} {medicine.dosage} - {medicine.boxes} caixas")


if __name__ == "__main__":
    main()
