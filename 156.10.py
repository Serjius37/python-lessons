#!/usr/bin/python3
'''
На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
Формат входных данных 
На вход программе подается натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание 1. Используйте встроенные функции bin(), oct(), hex().
Примечание 2. Для шестнадцатеричной системы счисления используйте заглавные буквы A, B, C, D, E, F.
Примечание 3. BOH = Binary, Octal, Hex.
'''

a = int(input())
print(bin(a)[2:],oct(a)[2:],hex(a)[2:].upper(),sep='\n')