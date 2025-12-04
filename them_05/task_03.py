# Совершите необходимые импорты
from datetime import datetime


records = {'А001АА': datetime(2024, 5, 27, 10, 0, 0),
           'А002АА': datetime(2024, 5, 27, 12, 31, 0),
           'А003АА': datetime(2024, 5, 27, 15, 20, 0), }

def road_payment(records: dict, car_number, dt: datetime):
    if car_number not in records:
        records[car_number] = dt
        return f'Автомобиль {car_number} зарегистрирован в {dt}'
    else:
        time_pay = dt - records[car_number]
        pay = int(time_pay.total_seconds() // 60) * 5
        del records[car_number]
        return f'Автомобиль {car_number} оплатил {pay} руб. в {dt}'


print(road_payment(records, 'А001АА', datetime(2024, 5, 27, 10, 10, 0)))
# Автомобиль А001АА оплатил 50 руб. в 2024-05-27 10:10:00
print(road_payment(records, 'А004АА', datetime(2024, 5, 27, 16, 10, 0)))
# Автомобиль А004АА зарегистрирован в 2024-05-27 16:10:00
print(road_payment(records, 'А003АА', datetime(2024, 5, 27, 22, 42, 0)))
# Автомобиль А003АА оплатил 2210 руб. в 2024-05-27 22:42:00