#!/usr/bin/python3
'''
На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.
Формат входных данных
На вход программе подается натуральное число nn.
Формат выходных данных
Программа должна вывести список, состоящий из делителей введенного числа.
'''

a = int(input())
i = 2
array = [1] 
while a != i:
    if a % i == 0:
        array.append(i)
    i += 1
array.append(a)        
print(array)