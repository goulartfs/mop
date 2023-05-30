import hashlib
from typing import List

from domain.entities.price import Price


class Medicine:
    """Medicine
    """

    def __init__(self,
                 name: str,
                 dosage: str,
                 boxes: int = 2,
                 prescription: bool = False,
                 prices: List[Price] = None):
        """init

        Args:
            name (str): medicine's name
            dosage (str): medicine's dosage
            boxes (int, optional): number of boxes want buy. Defaults to 2.
            prescription (bool, optional): prescription? Defaults to False.
            prices (List[Price], optional): medicine's price. Defaults to None.
        """
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
        """md5 hashed name

        Returns:
            str: hash
        """
        md5_hash = hashlib.md5()
        md5_hash.update(self.name.encode('utf-8'))
        return md5_hash.hexdigest()

    def update_price(self, new_price: Price) -> None:
        """update the medicine price by keeping a history

        Args:
            new_price (Price): new price
        """
        self.prices.append(new_price)

    def price(self) -> Price:
        """returns the last price registered

        Returns:
            Price: medicine's price
        """
        if self.prices:
            return self.prices[-1]
        return Price()
