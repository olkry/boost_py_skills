# Объявите функцию very_scary() с параметрами a, b
# Верните результат согласно формуле
# Выведите на экран только результат
def very_scary(a, b):
    summary = (((a * b) + ((a - b)**2))**3 / ((b**3)*(((a**2)+b)**2)))
    return summary


print(very_scary(5, 3))
# 0.3240268329554044
print(very_scary(-1, 3))
