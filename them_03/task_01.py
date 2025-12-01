# Объявите функцию fizz_buzz() с параметром x
# сделайте print() внутри тела функции исходя из полученного x
def fizz_buzz(x):
    if (x % 5 == 0) and (x % 3 == 0):
        x = 'fizz buzz'
    elif x % 5 == 0:
        x = 'buzz'
    elif x % 3 == 0:
        x = 'fizz'
    print(x)


fizz_buzz(15) # fizz buzz
fizz_buzz(2) # 2
fizz_buzz(3) # fizz
fizz_buzz(5) # buzz