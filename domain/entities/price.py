class Price:
    def __init__(self,
                 value: float = 0.0,
                 currency: str = "BRL",
                 symbol: str = "R$"):
        self.value = value
        self.currency = currency
        self.symbol = symbol
