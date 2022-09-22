# вариант человек против бота c интеллектом:


from random import randint

def input_date(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while 1 < x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def new_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player_1 = input("Введите имя первого игрока: ")
player_2 = "Mr.Candyman"
value = int(input("Введите количество конфет на столе: "))
randomizer = randint(0,2) # флаг очередности
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
        k = bot_calc(value)
        counter_2 += k
        value -= k
        randomizer = True
        new_print(player_2, k, counter_2, value)

if randomizer:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")