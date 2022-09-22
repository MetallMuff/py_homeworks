#  2.Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint


def input_date(name):
    x = int(input(f"{name}, Введите количество конфет, которое возьмете от 1 до 28: "))
    while 1 < x > 28:
        x = int(input(f"{name}, Введите корректное количество конфет: "))
    return x


def new_print(name, k, counter, value):
    print(f"Ход {name}, он взял {k} конфет, теперь у него {counter}. На столе осталось {value} конфет.")


player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
randomizer = randint(0, 2)
if randomizer:
    print(f"Первый ходит {player_1}")
else:
    print(f"Первый ходит {player_2}")

counter_1 = 0
counter_2 = 0

while value > 28:
    if randomizer:
        k = input_date(player_1)
        counter_1 += k
        value -= k
        randomizer = False
        new_print(player_1, k, counter_1, value)
    else:
        k = input_date(player_2)
        counter_2 += k
        value -= k
        randomizer = True
        new_print(player_2, k, counter_2, value)

if randomizer:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")
