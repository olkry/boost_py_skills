# Объявите функцию cash_counter() с параметром withdrawal
def cash_counter(withdrawal):
    # Объявите переменную is_correct_enter, в которую запишите True, если withdrawal кратен 100
    is_correct_enter = True if withdrawal % 100 == 0 else False
# Объявите переменные cash_100, cash_500, cash_1000 и посчитайте их значения
    cash_1000 = withdrawal // 1000
    cash_500 = (withdrawal % 1000) // 500
    cash_100 = (withdrawal % 500) // 100
# Выведите результат на экран в указанном в задаче формате
    print(
        f'Купюр номиналом 100: {cash_100}\n'
        f'Купюр номиналом 500: {cash_500}\n'
        f'Купюр номиналом 1000: {cash_1000}'
    )
# Верните переменную is_correct_enter
    return is_correct_enter


print(cash_counter(1501))
# Купюр номиналом 100: 0
# Купюр номиналом 500: 1
# Купюр номиналом 1000: 1

# False

