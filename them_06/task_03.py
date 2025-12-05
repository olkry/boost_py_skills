# Объявите функцию is_valid_password()
def is_valid_password(password: str):

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~"
    letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_lower = letters_upper.lower()
    digits = '0123456789'
    # Напишите решение и верните результат
    if ' ' in password or not (8 <= len(password) <= 16):
        return False

    sp, up, low, dig = False, False, False, False
    for char in password:
        if char in special_chars:
            sp = True
        elif char in letters_upper:
            up = True
        elif char in letters_lower:
            low = True
        elif char in digits:
            dig = True
    return (sp and up and low and dig)



print(is_valid_password("ValidP@ss1234"))  # True
print(is_valid_password("invalid"))  # False
print(is_valid_password("NoSpecial123456"))  # False
print(is_valid_password("noupper@1234"))  # False
print(is_valid_password("NOLOWER@1234"))  # False
print(is_valid_password("Short@1"))  # False
print(is_valid_password("TooLongPassword@123456789"))  # False
print(is_valid_password("Space @1234"))  # False
print(is_valid_password("Кириллица@1234"))  # False
