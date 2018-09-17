# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

import re

test_str = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

lower_letter = re.compile(r'[a-z]{2}([A-Z]+)[A-Z]{2}')
test1 = lower_letter.findall(test_str)

list1 = []
local_str = ''

current_state = 0 # ожидаем вхождения символа в нижнем регистре
j = 0

for i in test_str:
    if current_state == 0 and i.islower():
        current_state = 1 # вхождение 1-го символа в нижнем регистре
    elif current_state == 1 and i.islower():
        current_state = 2 # вхождение 2-го и более символов в верхнем регистре после состояния 1
    elif current_state == 1 and i.isupper():
        current_state = 0 # ожидаем вхождения символа в нижнем регистре
    elif current_state == 2 and i.islower():
        current_state = 2 # вхождение 2-го и более символов в верхнем регистре после состояния 1
    elif current_state == 2 and i.isupper():
        current_state = 3 # вхождение символа в вехнем регистре после 2 и более символов в нижнем
        index1 = j
    elif current_state == 3 and i.islower():
        current_state = 1
    elif current_state == 3 and i.isupper():
        current_state = 4 # вхождение символа в вехнем регистре после 1-го символа в верхнем регистре
    elif current_state == 4 and i.islower():
        current_state = 1
    elif current_state == 4 and i.isupper():
        current_state = 5 # вхождение символа в вехнем регистре после 2 и более символов в верхнем регистре
    elif current_state == 5 and i.islower():
        current_state = 1
        list1.append(test_str[index1: j - 2])
    elif current_state == 5 and i.isupper():
        current_state = 5
    j += 1

print(test1)
print(list1)
print( test1 == list1)