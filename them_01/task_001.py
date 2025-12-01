# Создайте переменные bananas_in_fridge, apples_in_fridge, oranges_in_fridge,
# обозначающие изначальное количество фруктов в холодильнике.
# Задайте им значения согласно условию задачи.

bananas_in_fridge = 12
apples_in_fridge = 14
oranges_in_fridge = 8

# Посчитайте общее количество фруктов в холодильнике изначально и
# запишите значение в переменную total_fruits_in_fridge.

total_fruits_in_fridge = (
    bananas_in_fridge + apples_in_fridge + oranges_in_fridge
)

# Создайте переменные bananas_in_basket, apples_in_basket, oranges_in_basket,
# обозначающие количество фруктов в корзине и
# определите их значения согласно условию задачи.

bananas_in_basket = 2
apples_in_basket = 3
oranges_in_basket = 1

# Посчитайте общее количество фруктов в одной корзине и запишите результат в
# переменную total_fruits_in_basket.

total_fruits_in_basket = (
    bananas_in_basket + apples_in_basket + oranges_in_basket
)


# Посчитайте оставшееся в холодильнике количество фруктов и запишите результат
# в переменную result.

result = total_fruits_in_fridge - (total_fruits_in_basket * 3)


# Выведите результат на экран в формате, указанном в условии задачи.

print(f'Фруктов в холодильнике осталось: {result}')
