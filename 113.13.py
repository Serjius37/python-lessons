#!/usr/bin/python3
'''
На вход программе подается натуральное число nn и nn строк, а затем число kk. Напишите программу, которая выводит kk-ую букву из введенных строк на одной строке без пробелов.
Формат входных данных
На вход программе подается натуральное число nn,  далее nn строк, каждая на отдельной строке. В конце вводится натуральное число kk – номер буквы (нумерация начинается с единицы).
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.
'''


sc = ''
array = [int(input()) for _ in range (int(input()))]
q = int(input())
for k in array: 
    if len(k) >= q:
        sc += k[q - 1]
print(sc)