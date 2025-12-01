# Объявите функцию buy_sweeties в параметре money
def buy_sweeties(money):
    # Посчитайте результат и напечатайте на экране фразу в соответствии с заданием
    chyp_cost = 5
    gum_cost = 2
    chyp_total = money // chyp_cost
    gum_total = (money % chyp_cost) // gum_cost
    print(f'На {money} руб. Вася может купить:'
          f'\nЧупа чупсов: {chyp_total} шт.'
          f'\nЖевательных резинок: {gum_total} шт.')


buy_sweeties(13)
# На 13 руб. Вася может купить:
# Чупа чупсов: 2 шт.
# Жевательных резинок: 1 шт.
buy_sweeties(1)
buy_sweeties(25)
