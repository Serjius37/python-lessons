#!/usr/bin/python3
'''
На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.
Формат входных данных
На вход программе подается натуральное число nn.
Формат выходных данных
Программа должна вывести список, состоящий из делителей введенного числа.
'''

a = int(input())
for i in range(2, a / 2 + 1):
    if a %i == 0:
        array.append(i)
array.append(a)        
print(array)