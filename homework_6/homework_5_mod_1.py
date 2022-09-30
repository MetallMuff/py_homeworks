# Вычисление максимального значения между двумя числами
maximum = (lambda a, b: a if a>b else b)
print('Максимальное число:', maximum(15, 13))

# Минимальное значение между тремя числами a, b, c
min = (lambda a, b, c: a if (a<=b)and(b<=c) else (b if (b<=a)and(b<=c) else c))
print('Минимальное число:', min(9,8,5))