from datetime import datetime


SERVICES = {
    'маникюр': 2000,
    'педикюр': 2500,
    'брови': 1500,
    'ресницы': 1000,
    'массаж тела': 5000
}


def update_schedule(
        dt: datetime,
        name: str,
        service: str,
        schedule: dict,
        services: dict,
        price: int = 0
):

    date = dt.strftime('%d.%m')
    time = dt.strftime('%H:%M')
    correct_service = service.lower()
    if correct_service not in services and price == 0:
        return 'Запись не добавлена! Укажите стоимость услуги.'

    final_price = (SERVICES[correct_service]
                   if correct_service in SERVICES else price)
    new_record = {
        'time': time,
        'name': name,
        'service': correct_service,
        'price': final_price
    }

    if date not in schedule:
        schedule[date] = []

    schedule[date].append(new_record)
    messege = (
        f'На {date} добавлена новая запись: {name} на {correct_service} '
        f'в {time}. Стоимость: {final_price}'
    )
    return messege


schedule = {}

dt = datetime(2025, 1, 15, 15, 30)
print(update_schedule(datetime(2025, 1, 15, 15, 30),
                      "Маша К.",
                      'Ноготочки',
                      schedule,
                      SERVICES,
                      0))  # Запись не добавлена! Укажите стоимость услуги.
print(update_schedule(datetime(2025, 1, 15, 15, 30),
                      "Маша К.",
                      'Ноготочки',
                      schedule,
                      SERVICES,
                      # На 15.01 добавлена новая запись: Маша К. на ноготочки в 15:30. Стоимость: 1000.
                      1000))
print(update_schedule(datetime(2025, 1, 15, 18, 00),
                      "Ира П.",
                      'педикюр',
                      schedule,
                      SERVICES,
                      # На 15.01 добавлена новая запись: Ира П. на педикюр в 18:00. Стоимость: 2500.
                      0))
