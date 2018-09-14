# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    fib_list = [1, 1]

    for i in range(m - 2):
        fib_list.append(fib_list[i] + fib_list[i + 1])

    return fib_list[n-1:m + 1]

n = int(input('n: '))
m = int(input('m: '))

print(fibonacci(n, m))