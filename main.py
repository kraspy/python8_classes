from shop import Product, Customer, Order, Discount


def main():
    # Продукты
    bread = Product('Хлеб', 400)
    coffee = Product('Кофе', 500)
    milk = Product('Молоко', 80)
    cheese = Product('Сыр', 120)

    discount10 = Discount('Сезонная скидка', 10)
    discount20 = Discount('Скидка по промокоду', 20)
    discount30 = Discount('Скидка за самовывоз', 15)

    customer1 = Customer(
        'Мария',
        orders=[
            Order([bread, coffee, milk]),
            Order([cheese]),
        ],
    )
    customer1.orders[0].apply_discount(discount10)

    customer2 = Customer(
        'Вася',
        orders=[
            Order(
                [bread, cheese],
            ),
        ],
    )
    customer2.orders[0].apply_discount(discount20)

    customer3 = Customer(
        'Андрей',
        orders=[
            Order(
                [coffee],
            ),
        ],
    )
    customer3.orders[0].apply_discount(discount30)

    print('-------------------')
    print('Приходили клиенты:')
    print(f'- {customer1}')
    print(f'- {customer2}')
    print(f'- {customer3}')
    print('-------------------')
    print(f'Общая стоимость заказов: {Order.get_total_price()} р.')
    print(f'Кол-во заказов: {Order.get_order_num()}')
    print('-------------------')


if __name__ == '__main__':
    main()
