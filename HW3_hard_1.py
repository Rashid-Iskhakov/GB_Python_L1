# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3



def convert (list1):
    negative = 1

    if is_negative(list1) == True:
        list_support = list1[0]
        list1[0] = list_support[1:]
        negative = -1
    else:
        pass

    if fraction_type(list1) == 1:
        fraction = [int(list1[0]) * negative, 1]
    elif fraction_type(list1) == 2:
        numerator, _, denominator = list1[2].partition('/')
        fraction = [(int(list1[0]) * int(denominator) + int(numerator)) * negative, int(denominator)]
    elif fraction_type(list1) == 3:
        numerator, _, denominator = list1[0].partition('/')
        fraction = [int(numerator) * negative, int(denominator)]

    return fraction

def fraction_type (list1):
    if '/' not in list1[0] and list1[2] == '':
        return 1 #только целая часть
    elif '/' in list1[2]:
        return 2 #целая и дробная часть
    elif '/' in list1[0]:
        return 3 #только дробная часть


def is_negative (list1):
    if '-' in list1[0]:
        return True
    else:
        return False

fraction = input('Введите выражение в формате n x/y + n x/y: ').strip()

if '+' in fraction:
    list1 = list(i.strip() for i in fraction.partition('+'))
elif '-' in fraction:
    list1 = list(i.strip() for i in fraction.partition('-'))

list2 = convert(list1[0].partition(' '))
list3 = convert(list1[2].partition(' '))
list4 = [list2[0] * list3[1], list2[1] * list3[1]]
list5 = [list3[0] * list2[1], list3[1] * list2[1]]

if '+' in fraction:
    list6 = [list4[0] + list5[0], list4[1]]
elif '-' in fraction:
    list6 = [list4[0] - list5[0], list4[1]]

n = list6[0] // list6[1]
x = list6[0] % list6[1]
y = list6[1]

print('{} {}/{}'.format(n, x, y))





#list = ['-1', '-1 1/5', '-1/5', '1', '1 1/5', '1/5']

#for i in list:
#    print(i.partition(' '))
