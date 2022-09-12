# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).

# Пример:

# 0,56 -> 11

# float_num = input('Введите вещественное число: ')
# print('Вы ввели число: ' + float_num)
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print('Сумма всех цифр: '+ str(sum))

# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# n = int(input('Введите число N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end= ' ')


# 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# Просим ввести количество чисел в последовательности
# k = int(input('Введите количество чисел в последовательности: '))
# numbers = []
# for i in range(0, k):
#     input_value = int(input(f'Введите число №{i}: '))
#     numbers.append(input_value)
# sum = 0
# for i in numbers:
#     sum = (1+1/k)**k
#  
# print('Сумма всех чисел последовательности:', round(sum, 4))


#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# arr = [int(input('Введите элемент списка: ')) for i in range(int(input('Введите длину списка: ')))]
#  
# prod = 1
# for i in arr:
#     prod *= i
#  
# print(f'Весь список: {arr}')
# print(f'Сумма элементов списка равна: {sum(arr)}')
# print(f'Произведение элементов списка: {prod}')

#  5. Реализуйте алгоритм перемешивания списка.

# import random
# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     return list
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Исходный список: ", list)
# print("Перемешанный список: ", mixed_list)

