#!/usr/bin/python3
'''
На вход программе подается одно число nn. Напишите программу, которая выводит список, состоящий из nn букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
Формат входных данных
На вход программе подается натуральное число n, n≤26n,n≤26.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

n = int(input())
a = list(range(97,97 + n))
print(a)
a = map(chr, a)
a = list(a)
print(a)
