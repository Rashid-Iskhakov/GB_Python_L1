# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

ticket_number = input('Введите номер билета: ')

def lucky_ticket(ticket_number):

    try:
        if len(ticket_number) == 6 and ticket_number.isdigit() == True:
            ticket_list = [int(i) for i in ticket_number]
            left_sum = sum(ticket_list[:3])
            right_sum = sum(ticket_list[3:])
        else:
            raise ValueError

        if left_sum == right_sum:
            return True
        else:
            return False

    except ValueError:
        print('Некорректный номер')
        exit(1)



if lucky_ticket(ticket_number) == True:
    print('Билет выиграл!')
else:
    print('Билет не выиграл')

