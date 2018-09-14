# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                (origin_list[i], origin_list[i + 1]) = (origin_list[i + 1], origin_list[i])
        n += 1
    return origin_list

origin_list = [float(i) for i in input('Введите список чисел через \',\': ').split(',')]

print(sort_to_max(origin_list))