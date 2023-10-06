class Drink:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.name + " : €" + str(self.price)


class AlcoholicDrink(Drink):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self) -> str:
        return super().__str__() + "\U0001F378"

