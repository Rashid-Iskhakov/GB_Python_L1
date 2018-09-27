"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


def get_random_card():
    l = list(range(1, 91))
    random.shuffle(l)
    line = l[0:15]
    return line

def shuffle_numbers():
    random_numbers = list(range(1, 91))
    random.shuffle(random_numbers)
    return random_numbers

def play_round(random_numbers, round_num, card1, card2):
    print(f'Новый бочонок: {random_numbers[round_num]} (осталось {90 - round_num - 1})')
    card1.print_card()
    card2.print_card()
    return random_numbers[round_num]

class Loto_card:
    def __init__(self, player, card):
        self.player = player
        self.card = card

    def is_in_card(self, num):
        if num in self.card:
            return True
        else:
            return False

    def print_card(self):
        line1 = sorted(self.card[0:5])
        line2 = sorted(self.card[5:10])
        line3 = sorted(self.card[10:15])
        heading = f'----Карточка {self.player}----'

        print(f'{heading:^26}')
        print(f'  {line1[0]} {line1[1]} {line1[2]}        {line1[3]} {line1[4]:>5}')
        print(f' {line2[0]}    {line2[1]}    {line2[2]} {line2[3]}    {line2[4]}')
        print(f'   {line3[0]} {line3[1]} {line3[2]}    {line3[3]} {line3[4]:>8}')
        print('--------------------------')

class game:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def points_num(self, num, points1 = 0, points2 = 0):
        if self.card1.is_in_card(num):
            points1 += 1
        if self.card2.is_in_card(num):
            points2 += 1
        return (points1, points2)


points_human = 0
points_computer = 0

loto_card_player = Loto_card('player', get_random_card())
loto_card_computer = Loto_card('computer', get_random_card())
loto_game = game(loto_card_player, loto_card_computer)

round = 0

num_sequence = shuffle_numbers()
print(num_sequence)

while max(points_human, points_computer) < 15:
    choosen_num = play_round(num_sequence, round, loto_card_player, loto_card_computer)

    answer = input('Зачеркнуть цифру? (y/n) ')
    print('')

    if answer == 'y' and loto_card_player.is_in_card(choosen_num):
        pass
    elif answer == 'n' and not loto_card_player.is_in_card(choosen_num):
        pass
    else:
        print('Вы проиграли')
        break

    points = loto_game.points_num(choosen_num)
    points_human += points[0]
    points_computer += points[1]

    print(f'player {points_human}:{points_computer} computer')

    round += 1

if points_human > points_computer:
    print(f'Вы победили со счетом {points_human}:{points_computer}')
elif points_human < points_computer:
    print(f'Вы проиграли со счетом {points_human}:{points_computer}')
elif points_human == points_computer == 15:
    print('Ничья')






