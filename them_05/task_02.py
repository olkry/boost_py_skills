car_numbers = ['111', '322', '541', '505']


def add_new_car(numbers: list, new_car_number: str):
    car_num = new_car_number[1:4]
    message = 'Добавлен новый автомобиль с номером '
    if car_num not in numbers:
        numbers.append(car_num)
        message += car_num
    else:
        if new_car_number in numbers:
            return 'Ты не пройдёшь!'
        numbers.append(new_car_number)
        message += new_car_number
    return message


# Добавлен новый автомобиль с номером А111ЕЕ140
print(add_new_car(car_numbers, 'А111ЕЕ140'))
# Добавлен новый автомобиль с номером 123
print(add_new_car(car_numbers, 'А123ЕЕ140'))
# Добавлен новый автомобиль с номером А123ЕЕ140
print(add_new_car(car_numbers, 'А123ЕЕ140'))
print(add_new_car(car_numbers, 'А123ЕЕ140'))  # Ты не пройдёшь!
