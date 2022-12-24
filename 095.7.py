#!/usr/bin/python3
'''
Дополните приведенный код, используя форматирование строк с помощью метода format, так чтобы он вывел текст: 
«In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
'''

s = 'In {0}, someone paid {1} {2} for two pizzas.'
n = 2010
a = '10k'
p = 'Bitcoin'
print(s.format(n, a, p))
