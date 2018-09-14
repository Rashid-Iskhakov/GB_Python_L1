# Задача-3:# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = [1, -4, 6, 8, -10, -9]

def user_filter (list, func):
    list1 =[]
    for i in list:
        if func(i) == True:
            list1.append(i)
    return list1


def func(x):
    if x < 0:
        return True
    else:
        return False

b = user_filter(a, func)
#b = list(b)
print(b)
