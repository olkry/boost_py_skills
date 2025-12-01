# Объявите функцию is_enought_machines() с указанными в условии параметрами
# return код сравнения, которое определит хватит ли машин
def is_enought_machines(free_machines_number, target_weight, max_payload=3):
    return (free_machines_number * max_payload) >= target_weight

print(is_enought_machines(3, 9, 11))
# True
print(is_enought_machines(1, 9, 3))
# False