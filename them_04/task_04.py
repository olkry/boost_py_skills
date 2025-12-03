# Произведите необходимые импорты и установите точность вычислений
import datetime
from decimal import Decimal, getcontext

fmt = '%H:%M'
# THREE_PLACES = Decimal('0.001')
getcontext().prec = 3


# Объявите функцию currency_converter() с указанными в задаче параметрами
# Выполните проверку корректности ввода

# Создайте переменные amount_dec, rate_dec и запишите в них Decimal значения соответствующих входных параметров

# Создайте переменную night_start и запиши в нее время начала ночи

# Создайте переменную night_end и запиши в нее время окончания ночи

# Создайте переменную is_night и запишите в нее True если сейчас ночь, иначе False

# Если сейчас ночь, то совершите необходимые действия из условия задачи

# Рассчитайте результат


def currency_converter(convert_time, amount, currency_rate):
    time_now = datetime.datetime.strptime(convert_time, fmt).time()
    errors = ''
    if amount <= 0:
        errors += 'amount '
    if currency_rate <= 0:
        errors += 'currency_rate '
    if errors:
        return errors + 'не может быть меньше или равно 0.'

    amount_dec = Decimal(str(amount))
    rate_dec = Decimal(str(currency_rate))
    night_start = datetime.time(hour=1)
    night_end = datetime.time(hour=8)
    is_night = True if night_start <= time_now < night_end else False
    if is_night:
        rate_dec *= Decimal('1.05')
    return (amount_dec * rate_dec)  #.quantize(THREE_PLACES)


# amount не может быть меньше или равно 0.
print(currency_converter("10:00", -5, 1.5))
# currency_rate не может быть меньше или равно 0.
print(currency_converter("10:00", 100, 0))
print(currency_converter("03:00", 100, 1))  # 105
print(currency_converter("00:59", 100, 1))  # 100
print(currency_converter("08:00", 100, 1))  # 100
print(currency_converter("14:59", 50000, 3))  # 1.50E+5
