# Применение лямбда-выражения и функции filter() для списка

list_1 = [ 8, 15, 7, 3, 11, 23, 187, -5, 20, 17 ]

list_2 = list(filter((lambda t: (t>=10)and(t<=20)), list_1))
print("list_2 = ", list_2)

def Range_10_20(t):
    return (t>=10)and(t<=20)

list_3 = list(filter(Range_10_20, list_1))
print("list_3 = ", list_3)