#!/usr/bin/python3
'''
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента 
строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
'''

# объявление функции
def convert_to_python_case(text):
    text = ['_' + text[i].lower() if text[i] in text[i].upper() and i != 0 and not text[i].isdigit() else text[i].lower() for i in range(len(text))]
    return text

# считываем данные
txt = input()

# вызываем функцию
print(*convert_to_python_case(txt), sep = '')