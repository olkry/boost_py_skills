# Объявите функцию vitya_hochet_viyti() с указанными в задании параметрами
# Заполните тело функции исходя из условий задачи
# Вызовите функцию
def vitya_hochet_viyti(degree, wind_speed, is_raining,
                       is_friend_calling, is_girl_abuse):
    if is_girl_abuse:
        return 'Уже бегу'
    if is_friend_calling and (degree >= -10 and wind_speed <= 20 and
                              not is_raining):
        return 'Зачилю с бро'
    if (degree >= 15 and wind_speed <= 15 and not is_raining):
        return 'Погуляю один'
    else:
        return 'Полежу дома'


print(vitya_hochet_viyti(-50, 100, True, True, True))  # "Уже бегу"
print(vitya_hochet_viyti(0, 10, True, True, False))  # "Полежу дома"
print(vitya_hochet_viyti(-5, 15, False, True, False))  # "Зачилю с бро"
print(vitya_hochet_viyti(20, 10, False, False, False))  # "Погуляю один"
