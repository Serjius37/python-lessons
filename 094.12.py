'''
На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
Формат входных данных 
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.
'''

s = input() 
if '.' in s[-3] and 'r' in s[-2] or '.' in s[-4] and 'c' in s[-3]:
    print('YES')
else :
    print('NO')
