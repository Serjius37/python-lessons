#!/usr/bin/python3
'''
На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 
Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
Формат выходных данных
Программа должна вывести две строки текста в соответствии с условием задачи.
'''

a = [int(i) for i in input().split()]
a.sort()
print(*a)
a.sort(reverse = True)
print(*a)

