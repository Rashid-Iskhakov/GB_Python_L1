# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random
import re

n = 2500
random_number = ''

for i in range(n):
    random_number = random_number + str(random.randint(0, 9))

path = os.path.join('D:\!Education\Python\Geekbrains\Level 1\Lesson 4', 'random_number.txt')
f = open(path, 'w', encoding='UTF-8')
f.write(random_number)
f.close()

f = open(path, 'r', encoding='UTF-8')
random_number = f.read()
print(random_number)

sequence = re.compile('[1]{2,2500}|[2]{2,2500}|[3]{2,2500}|[4]{2,2500}|[5]{2,2500}|[6]{2,2500}|[7]{2,2500}|[8]{2,2500}|[9]{2,2500}')

seq_lst = sequence.findall(random_number)
print(seq_lst)

seq_length = 0
j = -1
for i in seq_lst:
    j += 1
    if len(i) > seq_length:
        seq_length = len(i)
        num = j

print(seq_lst[num])