#!/usr/bin/python3
'''
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает из указанных строк список и выводит его.
Формат входных данных
На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
Формат выходных данных
Программа должна вывести список состоящий из указанных строк.
'''

a = int(input())
i = 0
array = ['w'] * a
while a != i:
    array[i] = input()
    i += 1
print(array)