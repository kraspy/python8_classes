class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name}'

    def __eq__(self, other) -> bool:
        return self.price == other.price

    def __lt__(self, other) -> bool:
        return self.price < other.price
