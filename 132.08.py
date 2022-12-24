#!/usr/bin/python3
'''
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;

а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.
'''

def draw_triangle(fill, base):
    a = 1
    for i in range(1,base+1):
        if (base / 2) + 1 > i:
            print(fill * i)
        else :
            print(fill * (i - a * 2 ))
            a += 1
            
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)