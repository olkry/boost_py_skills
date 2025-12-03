# Произведите необходимые импорты и установите точность вычислений
from datetime import datetime, timedelta

# Объявите функцию get_arrival_time() с указанными в задаче параметрами
# Преобразуйте departure_time в datetime
# Преобразуйте hour и minute в timedelta
# Вычислите время прибытия и верните его


def get_arrival_time(departure_time, hour, minute):
    if not (0 <= hour < 24) or not (0 <= minute < 60):
        return 'Ошибка в данных'

    fmt = '%H:%M %d:%m:%Y'
    dep_time = datetime.strptime(departure_time, fmt)
    flight_duration = timedelta(hours=hour, minutes=minute)
    arrival_time = dep_time + flight_duration
    return arrival_time.strftime(fmt)



print(get_arrival_time("10:30 15:12:2023", 2, 45))  # "13:15 15:12:2023"
print(get_arrival_time("23:45 31:12:2023", 3, 30))  # "03:15 01:01:2024"
print(get_arrival_time("10:30 15:12:2023", -1, 45))  # "Ошибка в данных"
print(get_arrival_time("10:30 15:12:2023", 2, 60))   # "Ошибка в данных"
