from typing import List
    
class Price:
    def __init__(self,
                 value: float = 0.0,
                 currency:str = "BRL",
                 symbol:str = "R$"):
        self.value = value
        self.currency = currency
        self.symbol = symbol

class Medicine:
    def __init__(self, 
                 name: str, 
                 dosage: str,
                 boxes: int = 2,
                 prescription: bool = False,
                 prices: List[Price] = []):
        self.name = name
        self.dosage = dosage
        self.boxes = boxes
        self.prescription = prescription
        self.prices = prices

    def __eq__(self, other) -> bool:
        if isinstance(other, Medicine):
            return self.name == other.name and self.dosage == other.dosage
        return False
    
    def update_price(self, new_price: Price) -> None:
        self.prices.append(new_price)

    def price(self) -> Price:
        if self.prices:
            return self.prices[-1]
        return Price()

class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.medicines: List[Medicine] = []  # List of Medicine objects

    def add_medicine(self, medicine: Medicine) -> None:
        self.medicines.append(medicine)

    def remove_medicine(self, medicine: Medicine) -> None:
        print(f"Removing Medicine: {medicine.name}, Dosage: {medicine.dosage}")
        self.medicines.remove(medicine)


def main(*args, **kwargs):
    pharmacy = Pharmacy("ABC Pharmacy")

    pharmacy.add_medicine(Medicine("Besilato de anlodipino", "5mg"))
    pharmacy.add_medicine(Medicine("Prolopa HBS", "100/25mg"))
    pharmacy.add_medicine(Medicine("Prolopa BD", "100/25mg"))
    pharmacy.add_medicine(Medicine("Risperidona", "1mg", prescription=True))
    pharmacy.add_medicine(Medicine("Sivastatina", "40mg"))
    pharmacy.add_medicine(Medicine("AAS Protect", "100mg"))
    pharmacy.add_medicine(Medicine("Cloridrato de metformina", "500mg"))
    pharmacy.add_medicine(Medicine("Losartana potássica", "50mg"))


    # Access the medicines of the pharmacy
    print (f'Printing Medicine\'s list')
    for medicine in pharmacy.medicines:
        print(f"Medicine: {medicine.name} {medicine.dosage}")

    # Remove a medicine from the pharmacy
    pharmacy.remove_medicine(Medicine("Risperidona", "1mg", True))

    # Verify the updated list of medicines

    print (f'Printing Medicine\'s list\n\n')
    for medicine in pharmacy.medicines:
        print(f"- {medicine.name} {medicine.dosage} - {medicine.boxes} caixas")

if __name__ == "__main__":
    main()