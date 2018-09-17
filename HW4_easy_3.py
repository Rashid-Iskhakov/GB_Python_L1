# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

def filter_list (list1):
    list1 = [x for x in list1 if x % 3 == 0 and x > 0 and x % 4 != 0]
    return list1


test_list = [random.randint(-100, 100) for x in range(10)]
print('{} -> {}'.format(test_list, filter_list(test_list)))