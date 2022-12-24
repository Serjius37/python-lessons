#!/usr/bin/python3
'''
На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
Формат входных данных
На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем один поисковый запрос.
Формат выходных данных
Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
Примечание. Поиск не должен быть чувствителен к регистру символов.
'''

a = int(input())
i = j = 0
array = [''] * a
array1 = ['a']
while a != i:
    d = input()
    array[i] = d
    i += 1
v = input()
while a != j:
    if v.lower() not in array[j].lower():
        del array[j]
        a -= 1
    else:
        j += 1    
print(*array, sep = '\n')