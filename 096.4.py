#!/usr/bin/python3
'''
На вход программе подаются два числа aa и bb. Напишите программу, которая для каждого кодового значения в диапазоне от aa до bb (включительно), выводит соответствующий ему символ из таблицы символов Unicode.
Формат входных данных 
На вход программе подается два натуральных числа, каждое на отдельное строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

s = int(input())
a = int(input())
for i in range (s,a+1):
    print(chr(i),end = ' ')