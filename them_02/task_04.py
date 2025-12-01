# Объявите функцию get_pack_number() с указанными в задаче параметрами
# Учитывая процент брака посчитайте сколько нужно упаковок и верните результат
def get_pack_number(candies_number, candies_in_pack=15, defect_percent=5):
    candies_number = int(candies_number - (candies_number *
                                           (defect_percent / 100)))
    return int(candies_number // candies_in_pack)


print('Необходимое количество упаковок:', get_pack_number(100))
# Необходимое количество упаковок: 6