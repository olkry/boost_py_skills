class BankAccount:
    def __init__(self, account_number, owner,
                 initial_balance=0, currency="руб."):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount
        return f"Счет пополнен на {amount} {self.currency}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Со счета снято {amount} {self.currency}"
        return (f"Недостаточно средств! Доступно: {self.balance} "
                f"{self.currency}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (f"Счет: {self.account_number}, Владелец: {self.owner}, "
                f"Баланс: {self.balance} {self.currency}")


# Тестирование
# Создаем счета
account1 = BankAccount(
    "40702810500000000001",
    "Иван Иванов",
    1000)
account2 = BankAccount(
    "40702810500000000002",
    "Мария Петрова",
    5000,
    "USD")

# Проверяем создание
print(account1)
print(account2)

# Тестируем операции
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(2000))  # Должна быть ошибка - недостаточно средств

print(account2.deposit(1000))
print(account2.withdraw(2000))

# Проверяем итоговый баланс
print(f"Баланс счета 1: {account1.get_balance()} {account1.currency}")
print(f"Баланс счета 2: {account2.get_balance()} {account2.currency}")