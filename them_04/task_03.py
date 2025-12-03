import datetime

# Объявите функцию to_usual_time_format() с указанными в задаче параметрами
# Создайте переменную errors и инициализируйте ее пустой строкой
# Сделайте проверку входных параметров и при обнаружении ошибки добавьте значение параметра к строке в формате “<значение><пробел>”, например “-1 “
# Если есть ошибки, то верните строку в соответствии с условием задачи
# Выполните необходимые преобразования и верните результат


def to_usual_time_format(hour=0, minute=0, meridiem=None):
    errors = ''
    if not (0 <= minute < 60):
        errors += str(minute) + ' '
    if not (0 <= hour < 12):
        errors += str(hour) + ' '
    if not (meridiem == 'am' or meridiem == 'pm'):
        errors += meridiem + ' '
    if errors:
        return 'Некорректный ввод: ' + errors

    if meridiem == 'pm':
        hour += 12
    inp_time = datetime.time(hour=hour, minute=minute)
    return inp_time


print(to_usual_time_format(0, 0, 'am'))  # 00:00:00
print(to_usual_time_format(0, 0, 'pm'))  # 12:00:00
print(to_usual_time_format(11, 30, 'pm'))  # 23:30:00
print(to_usual_time_format(5, 45, 'am'))  # 05:45:00
