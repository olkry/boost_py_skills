# Объявите функцию count_calories() с параметрами, указанными в условии задачи.
def count_calories(banana_number=0, apple_number=0, orange_number=0):
    # Посчитайте суммарную калорийность всех фруктов 
    # и запишите в переменную total_calories
    total_calories = (
        105 * banana_number + 52 * apple_number + 62 * orange_number
    )

    # Выведите результат на экран в соответствующем формате
    print(f'Общая калорийность: {total_calories} ккал')

count_calories(banana_number=2, apple_number=3, orange_number=1)
# Общая калорийность: 428 ккал

count_calories(apple_number=5, orange_number=3)
# Общая калорийность: 446 ккал