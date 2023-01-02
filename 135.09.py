#!/usr/bin/python3
'''
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является
 правильной скобочной последовательностью и False в противном случае.
Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
'''

# объявление функции
def is_correct_bracket(text):
    c = 0
    for i in text:
        if '(' in i:
            c += 1
        else:
            c -= 1
        if c < 0:
            break
    if c == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))