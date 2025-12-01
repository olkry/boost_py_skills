# Объявить функцию get_length_from_perimeter с параметром perimeter - периметр квадрата
def get_length_from_perimeter(perimeter):
    return perimeter / 4
# Объявить функцию get_cube_volume с параметром side - длина стороны квадрата


def get_cube_volume(side):
    return side ** 3


# Определить переменную side как результат функции get_length_from_perimeter
side = get_length_from_perimeter(20)

# Вызвать функцию get_cube_volume() передав аргумент side и вывести результат в указанном формате
print('Объём куба:', get_cube_volume(side), 'м.')
