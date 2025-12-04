from random import randint


calories_dict = {
    'яблоко': 52,
    'банан': 89,
    'курица': 165,
    'рис': 130
}

# Объявите функцию jrun() с указанными в задаче параметрами

# Проверьте наличие ключа в словаре

# Верните результат в соответствии с заданием


def jrun(food_name: str, food_weight, calories_dict):
    name = food_name.lower()
    if name not in calories_dict:
        calories_dict[name] = randint(100, 600)

    calories = calories_dict[name] * (food_weight / 100)
    messege = (f'Количество калорий на {food_weight} грамм '
               f'в продукте "{food_name}" равно {calories}.')
    return messege


# Количество калорий на 200 грамм в продукте "ЯбЛоКо" равно 104.0.
print(jrun('ЯбЛоКо', 200, calories_dict))
# Количество калорий на 150 грамм в продукте "Авокадо" равно {случайное значение}.
print(jrun('Авокадо', 150, calories_dict))
