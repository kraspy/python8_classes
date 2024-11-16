from shop.order import Order


class Customer:
    def __init__(self, name: str, orders: list[Order] = []) -> None:
        self.name = name
        self.orders = orders

        print('********************')
        print(f'Клиент {self.name} пришел в магазин.')
        if len(self.orders) > 0:
            print(f'\n{self.name} оформил(а) заказы:')
            for order in self.orders:
                print(f'- {order}')
                for product in order.products:

                    print(f'\t- {product.name}: {product.price} р.')
            print(f'Общая стоимость заказов: {sum(order.calculate_order_price() for order in self.orders)} р.')
        else:
            print(f'{self.name} Ничего не купил(а).')

    def __str__(self):
        return f'Клиент: {self.name}. Кол-во заказов: {len(self.orders)}'
