#!/usr/bin/python3
'''
Remove outliers
При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
На вод программе подается натуральное число nn, а затем nn различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
Формат входных данных
На вход программе подаются натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

a = int(input())
i = 0
array = ['w'] * a
while a != i:
    d = int(input())
    array[i] = d
    i += 1
array.remove(max(array))
array.remove(min(array))
print(*array, sep = '\n')