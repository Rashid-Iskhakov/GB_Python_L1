
#Напишите функцию, которая считает сумму квадратов от своих аргументов.
#Кол-во аргументов функции может быть любым.

#def is_parallelogram (a, b, c, d)

def sum_sq (*args):
    sq_list = [i ** 2 for i in args]
    return sum (sq_list)

arg1 = float(input('arg1: '))
arg2 = float(input('arg1: '))
arg3 = float(input('arg1: '))

print(sum_sq(arg1, arg2, arg3))