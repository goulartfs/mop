from typing import List
from app.application import Application
from app.entities.pharmacy import Pharmacy
from app.entities.medicine import Medicine
from app.services.medicine_service import MedicineService
from infrastructure.memory.repositories.medicine_repository import MedicineRepository
from app.services.patient_service import PatientService
from infrastructure.memory.repositories.patient_repository import PatientRepository
    
def main(*args, **kwargs):
    application = Application(
        medicine_service=MedicineService(MedicineRepository()),
        patient_service=PatientService(PatientRepository())
    )

    pharmacy = Pharmacy("My Own Pharmacy")

    application.add_new_medicine(pharmacy, Medicine("Besilato de anlodipino", "5mg"))
    application.add_new_medicine(pharmacy, Medicine("Prolopa HBS", "100/25mg"))
    application.add_new_medicine(pharmacy, Medicine("Prolopa BD", "100/25mg"))
    application.add_new_medicine(pharmacy, Medicine("Risperidona", "1mg", prescription=True))
    application.add_new_medicine(pharmacy, Medicine("Sinvastatina", "40mg"))
    application.add_new_medicine(pharmacy, Medicine("AAS Protect", "100mg"))
    application.add_new_medicine(pharmacy, Medicine("Cloridrato de metformina", "500mg"))
    application.add_new_medicine(pharmacy, Medicine("Losartana potássica", "50mg"))

    print (f'Printing Medicine\'s list')
    for medicine in application.get_medicine_list(pharmacy):
        print(f"- {medicine.name} {medicine.dosage} - {medicine.boxes} caixas")

if __name__ == "__main__":
    main()