# Применение лямбда-выражения и функции map() для кортежа

T = ( 2.88, -1.75, 100.55 )

T2 = tuple(map((lambda x: int(x)), T))

print("T2 = ", T2)