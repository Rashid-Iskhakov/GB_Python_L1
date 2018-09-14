# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

import random

def my_round(number, ndigits):

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    try:
        if '.' in str(number):
            decimal_places = abs(str(number).find('.') - len(str(number))) - 1
        else:
            decimal_places = 0

        if is_number(number) == True and is_number(ndigits) == True and float(ndigits) % 1 == 0 and float(ndigits) >= 0:
            pass
        else:
            raise ValueError

        if int(ndigits) >= decimal_places:
            n3 = float(number)
        else:
            if float(number) < 0:
                n1 = str(number)[:str(number).find('.') + int(ndigits) + 3]
            elif float(number) >= 0:
                n1 = str(number)[:str(number).find('.') + int(ndigits) + 2]

            n2 = float(n1) * (10 ** (float(ndigits) + 1)) % 10
            if n2 >= 5:
                n3 = float(n1) * (10 ** (float(ndigits) + 1)) // 10 + 1
            else:
                n3 = float(n1) * (10 ** (float(ndigits) + 1)) // 10

            n3 = n3 / (10 ** float(ndigits))
        return n3
    except ValueError:
        print('Некорректные данные')

number = input('Введите число: ')
ndigits = input('Введите число разрядов: ')
my_round_to_str = '{:.' + str(ndigits) + 'f}'
print(my_round_to_str.format(my_round(number, ndigits)))

print()
print('---------- with random values: ----------')

number1 = random.uniform(-100, 100)
ndigits1 = random.randint(0, 10)
print('Число: ', number1)
print('Число разрядов: ', ndigits1)
print(my_round(number1, ndigits1))






