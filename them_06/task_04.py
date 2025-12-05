def bad_password(users: list[dict[list]]):
    warnings, criticals = [], []
    for user in users:
        full_name = f'{user['name']} {user['surname']}'
        if (
            user['birth_date'][-4:] in user['password'] and
            (
                user['name'][:3].lower() in user['password'].lower() or
                user['surname'][:3].lower() in user['password'].lower()
            )
        ):
            criticals.append(full_name)
        elif (
            user['birth_date'][-4:] in user['password'] or
            user['name'][:3].lower() in user['password'].lower() or
            user['surname'][:3].lower() in user['password'].lower()

        ):
            warnings.append(full_name)
    message = f'''warnings:
{'\n'.join(warnings)}
criticals:
{'\n'.join(criticals)}
'''
    return message[:-1]


users = [
    {'name': 'Michael', 'surname': 'Ivanov',
        'birth_date': '01.11.1999', 'password': 'Michael1999'},
    {'name': 'Anna', 'surname': 'Petrova',
        'birth_date': '15.05.1985', 'password': 'Anna1234'},
    {'name': 'John', 'surname': 'Smith',
        'birth_date': '20.03.1978', 'password': 'Smi1978John'}
]


print(bad_password(users))
#  warnings:
#  Anna Petrova
#  criticals:
#  Michael Ivanov
#  John Smith

'\nwarnings:\nOlga Sidorova\nDaniel Brown\nEmily Johnson\ncriticals:\nVictor Kuznetsov'
'warnings:\nOlga Sidorova\nDaniel Brown\nEmily Johnson\ncriticals:\nVictor Kuznetsov'