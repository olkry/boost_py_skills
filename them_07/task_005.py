class Order:
    def __init__(self, order_number, items=None):
        self.order_number = order_number
        self.items: list[dict] | None = items
        self.status = 'новый'
        self.discount = 0

    def add_item(self, name, price):
        product = {'name': name, 'price': price}
        if self.items is None:
            self.items = [product,]
        else:
            self.items.append(product)
        return f"Товар '{name}' добавлен в заказ"

    def calculate_total(self):
        total_price = 0
        if self.items:
            for prod in self.items:
                total_price += prod['price']
            if self.discount:
                total_price = total_price * (1 - self.discount / 100)
        return total_price

    def apply_discount(self, percent):
        self.discount = percent
        return f"Скидка {percent}% применена"

    def change_status(self, new_status):
        self.status = new_status
        return f"Статус заказа изменен на '{new_status}'"

    def get_order_info(self):
        return (f"Заказ #{self.order_number}, Статус: {self.status}, "
                f"Товаров: {len(self.items) if self.items else 0}, "
                f"Сумма: {self.calculate_total()} руб.")


# Тестирование
order1 = Order("2024-001")
order2 = Order("2024-002",
               [{"name": "Ноутбук", "price": 50000}])

print(order1.get_order_info())
print(order2.get_order_info())

order1.add_item("Мышь", 1500)
order1.add_item("Клавиатура", 3000)
order2.add_item("Чехол", 2000)

print(order1.apply_discount(10))
print(order2.apply_discount(5))

order1.change_status("обработан")
order2.change_status("доставлен")

print(order1.get_order_info())
print(order2.get_order_info())

print(f"Итоговая сумма заказа 1: {order1.calculate_total()} руб.")
print(f"Итоговая сумма заказа 2: {order2.calculate_total()} руб.")