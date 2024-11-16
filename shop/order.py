from . import Product


class Order:
    order_num = 0
    total_price = 0

    @classmethod
    def get_total_price(cls) -> int:
        return cls.total_price

    @classmethod
    def get_order_num(cls) -> int:
        return cls.order_num

    def __init__(self, products: list[Product]) -> None:
        self.order_num = Order.order_num + 1
        self.products = products
        Order.order_num += 1

    def __str__(self):
        return f'Заказ: #{self.order_num}'

    def calc_order_price(self) -> int:
        order_price = sum(product.price for product in self.products)
        return order_price

    def calculate_order_price(self) -> int:
        self.total_price = sum(product.price for product in self.products)
        Order.total_price += self.total_price
        return self.total_price

    def apply_discount(self, discount):
        order_price = self.calc_order_price()

        new_price = discount.calc_price_with_discount(order_price, discount)

        Order.total_price -= order_price
        Order.total_price += new_price
        print(f'Скидка "{discount.description}: {discount.discount_percent}%" применена к заказу #{self.order_num}')
        print(f'Стоимость заказа с скидкой: {new_price} р.')
        print(f'Общая стоимость заказов (со скидками): {Order.get_total_price()} р.')
        return self
