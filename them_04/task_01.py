# Импортируйте необходимый модуль
from datetime import datetime, timedelta

# Объявите функцию check_arrival_time() с параметрами current_time и lesson_start (по умолчанию "08:30")
# Преобразуйте входные параметры во время указав нужный формат
# Рассчитайте разницу во времени и преобразуйте ее в минуты
# Определите и верните соответствующее условию задачи сообщение

def check_arrival_time(current_time, lesson_start='08:30'):
    fmt = '%H:%M'
    come = datetime.strptime(current_time, fmt)
    lesson = datetime.strptime(lesson_start, fmt)
    diff_time = come - lesson

    minutes = int(diff_time.total_seconds() // 60)

    if minutes <= -60:
        return 'Ваш ребенок пришел слишком рано!'
    if minutes <= 0:
        return 'Ваш ребенок пришел в школу вовремя.'
    else:
        return f'Ваш ребенок опоздал на {minutes} мин.'


# Пример вызова функции
print(check_arrival_time("08:15"))  # Ваш ребенок пришел в школу вовремя.
print(check_arrival_time("06:30"))  # Ваш ребенок пришел слишком рано!
print(check_arrival_time("08:45"))  # Ваш ребенок опоздал на 15 мин.