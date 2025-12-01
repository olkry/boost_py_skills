# Объявите функцию count_discount() с указанными в задании параметрами
# Обработайте некорректный ввод
# Заполните тело функции исходя из условий задачи

def count_discount(goods_number, total_price):
    if goods_number <= 0 or total_price <= 0:
        return 'Ошибка ввода!'
    discount = 0.0
    if goods_number == 1:
        discount = total_price * 0.1
    elif 2 <= goods_number <= 4:
        discount = total_price * 0.15
    else:
        discount = total_price * 0.25
    total_price = total_price - discount
    return (f'Сумма общей скидки: {discount}, '
            f'а итоговая стоимость: {total_price}')


# Напечатайте результат
# Сумма общей скидки: 10.0, а итоговая стоимость: 90.0
print(count_discount(1, 100))
# Сумма общей скидки: 80.5, а итоговая стоимость: 241.5
print(count_discount(5, 322))
# Сумма общей скидки: 6.3, а итоговая стоимость: 35.7
print(count_discount(2, 42))
