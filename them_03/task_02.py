# Объявите функцию get_envelope() с указанными в задании параметрами
# Обработайте некорректный ввод
# Заполните тело функции исходя из условий задачи

def get_envelope(length, width):
    env_1 = 15, 10
    env_2 = 25, 15
    env_3 = 34, 22
    envelop = 'Подходящий конверт '
    if length < width:
        length, width = width, length
    if length <= env_1[0] and width <= env_1[1]:
        envelop += '1'
    elif length <= env_2[0] and width <= env_2[1]:
        envelop += '2'
    elif length <= env_3[0] and width <= env_3[1]:
        envelop += '3'
    else:
        envelop += 'не найден'
    return envelop


# Напечатайте результат
print(get_envelope(5, 16))   # Подходящий конверт 2
print(get_envelope(30, 15))  # Подходящий конверт 3
print(get_envelope(35, 23))  # Подходящий конверт не найден