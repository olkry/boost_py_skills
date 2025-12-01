# Объявите функцию get_triangle_info() с указанными в задании параметрами
# Заполните тело функции исходя из условий задачи
# Напечатайте результат на экран

def get_triangle_info(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 'Ошибка ввода!'
    if a + b < c or b + c < a or c + a < b:
        return 'Треугольник невозможен'
    if a == b == c:
        return f'Треугольник равносторонний {a + b + c}'
    if a == b or b == c or a == c:
        other = a if b == c else (b if a == c else c)
        return f'Треугольник равнобедренный {other}'
    else:
        return f'Треугольник разносторонний {(a + b + c) / 3}'


print(get_triangle_info(2, 2.5, 3))  # Треугольник разносторонний 2.5
print(get_triangle_info(2, 2, 3))  # Треугольник равнобедренный 3
print(get_triangle_info(2, 2, 2))  # Треугольник равносторонний 6
print(get_triangle_info(1, 1, 3))  # Треугольник невозможен
print(get_triangle_info(-1, -2, -3))  # Ошибка ввода!
