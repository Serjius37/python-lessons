#!/usr/bin/python3
'''
На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.
Формат выходных данных
Программа должна вывести одно число – количество пар элементов, равных друг другу.
'''

s = input()
c = v = 0
b = s.split()
for i in b:
    for j in range(len(b)):
        if j == v :
            continue
        if i == b[j]:
            c += 1
    v += 1        
print(c//2)