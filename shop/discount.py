class Discount:
    @staticmethod
    def calc_price_with_discount(price, discount):
        new_price = price * (1 - discount.discount_percent / 100)
        return new_price

    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    def __str__(self):
        return f'{self.description}: {self.discount_percent}%'
