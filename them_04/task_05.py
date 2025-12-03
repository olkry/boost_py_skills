# Произведите необходимые импорты и установите точность вычислений
from datetime import datetime
from decimal import Decimal, getcontext

getcontext().prec = 3
# TWO_PLACES = Decimal('0.01')
'''
# Объявите функцию conversion_result() с указанными в задаче параметрами

    # Инициализируйте переменную now текущим временем

	# Исходя из условия задачи верните нужную строку

# Объявите функцию universal_converter() с указанными в задаче параметрами

	# Сделайте проверку вводных параметров

	# Исходя из введенного кода страны вызовите функцию conversion_result() с параметрами соответствующими этому коду
'''

COUNTRIES = {
    'DE': {
        'name': 'Германия',
        'currency': 'EUR',
        'rate_to_rub': Decimal('93.763'),
        'date_format': '%d.%m.%Y %H:%M Uhr'
    },
    'CN': {
        'name': 'Китай',
        'currency': 'CNY',
        'rate_to_rub': Decimal('11.164'),
        'date_format': '%Y-%m-%d %H:%M'
    },
    'US': {
        'name': 'США',
        'currency': 'USD',
        'rate_to_rub': Decimal('79.322'),
        'date_format': '%d/%m/%Y %H:%M'
    }
}


def conversion_result(
    dt_format, rub_amount, currency_rate: Decimal, currency_symbol
):
    now = datetime.now()
    local_time_str = now.strftime(dt_format)

    if rub_amount == 0:
        return (f"Местная дата и время: {local_time_str}, "
                f"местный курс к рублю: {currency_rate}")

    local_amount = Decimal(str(rub_amount)) / Decimal(str(currency_rate))

    return (f"Местная дата и время: {local_time_str}, "
            f"{rub_amount} RUB = {local_amount} {currency_symbol}")


def universal_converter(code: str, rub_amount=0):
    if rub_amount < 0:
        return f"Ошибка ввода: rub_amount {rub_amount}"

    code_up = code.upper()
    code_low = code.lower()

    if (code != code_up and code != code_low) or code_up not in COUNTRIES:
        return f'Ошибка ввода: code {code}'

    country_data = COUNTRIES[code_up]

    return conversion_result(
        dt_format=country_data['date_format'],
        rub_amount=rub_amount,
        currency_rate=country_data['rate_to_rub'],
        currency_symbol=country_data['currency']
    )


# Местная дата и время: 21.08.2025 23:24 Uhr, местный курс к рублю: 93.763
print(universal_converter('DE'))
# Местная дата и время: 21.08.2025 23:24 Uhr, 100 RUB = 1.07 EUR
print(universal_converter('DE', 100))
print(universal_converter('De', 100))  # Ошибка ввода: code De
# Местная дата и время: 21/08/2025 23:24, 322 RUB = 4.06 USD
print(universal_converter('us', 322))
print(universal_converter('cnn', -1))  # Ошибка ввода: rub_amount -1
