class WarehouseItem:
    def __init__(self, item_code, name, quantity, price):
        self.item_code = item_code
        self.name = name
        self.quantity = quantity
        self.price = price
        self.reserved = 0

    def reserve(self, amount):
        if self.quantity - self.reserved >= amount:
            self.reserved += amount
            return True
        return False

    def release(self, amount):
        if self.reserved >= amount:
            self.reserved -= amount
            return amount
        out_reserve = self.reserved
        self.reserved = 0
        return out_reserve

    def sell(self, amount):
        if self.reserved >= amount:
            self.reserved -= amount
            self.quantity -= amount
            return f"Продано {amount} единиц товара '{self.name}'"
        return (f'Недостаточно зарезервированного товара. '
                f'Зарезервировано: {self.reserved}')

    def get_available_quantity(self):
        return self.quantity - self.reserved

    def get_item_info(self):
        return (f"Товар: {self.name} (код: {self.item_code}), "
                f"Доступно: {self.quantity - self.reserved} "
                f"из {self.quantity}, Цена: {self.price} руб.")


# Тестирование
item1 = WarehouseItem(
    "A001",
    "Смартфон",
    50,
    25000)
item2 = WarehouseItem(
    "A002",
    "Планшет",
    20,
    40000)

print(item1.get_item_info())
print(item2.get_item_info())

# Тестируем резервирование
print(f"Резервирование 30: {item1.reserve(30)}")
print(f"Резервирование 25: {item1.reserve(25)}")  # Должно не удаться

# Тестируем продажи
print(item1.sell(10))
print(item2.sell(5))

# Тестируем освобождение резерва
released = item1.release(15)
print(f"Освобождено из резерва: {released}")

print(item1.get_item_info())
print(item2.get_item_info())

print(f"Доступно товара 1: {item1.get_available_quantity()}")
print(f"Доступно товара 2: {item2.get_available_quantity()}")
