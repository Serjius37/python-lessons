#!/usr/bin/python3
'''
Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).
'''

eywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m for m in keywords if len(m) >= 5]
print(new_keywords)
