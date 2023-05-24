import hashlib
from typing import List

from domain.entities.price import Price


class Medicine:
    def __init__(self,
                 name: str,
                 dosage: str,
                 boxes: int = 2,
                 prescription: bool = False,
                 prices: List[Price] = None):
        if prices is None:
            prices = []

        self.name = name
        self.dosage = dosage
        self.boxes = boxes
        self.prescription = prescription
        self.prices = prices

    def __eq__(self, other) -> bool:
        if isinstance(other, Medicine):
            return self.name == other.name and self.dosage == other.dosage
        return False

    @property
    def id(self) -> str:
        md5_hash = hashlib.md5()
        md5_hash.update(self.name.encode('utf-8'))
        return md5_hash.hexdigest()

    def update_price(self, new_price: Price) -> None:
        self.prices.append(new_price)

    def price(self) -> Price:
        if self.prices:
            return self.prices[-1]
        return Price()
