#!/usr/bin/python3
'''
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует
 зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными,
  а прописные – прописными.
Формат входных данных 
На вход программе подается строка текста на английском языке.
Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.
Примечание. Символы, не являющиеся английскими буквами, не изменяются.
'''
def is_magic1(s):
    v = s.split()
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for j in range(len(v)): 
        for i in range(len(v[j])):
            v[j] = list(v[j])
            w = "".join(c for c in v[j] if c.isalpha())
            if v[j][i] in a:
                v[j][i] = a[a.find(v[j][i]) + len(w)]
            if v[j][i] in b:
                v[j][i] = b[b.find(v[j][i]) + len(w)] 
def is_magic2(s):
    v = s.split()
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for j in range(len(v)): 
        for i in range(len(v[j])):
            v[j] = list(v[j])
            w = "".join(c for c in v[j] if c.isalpha())
            if v[j][i] in a:
                v[j][i] = a[a.find(v[j][i]) - len(w)]
            if v[j][i] in b:
                v[j][i] = b[b.find(v[j][i]) - len(w)]                 
s = input() 
if(fl) 
    is_magic1(s)
else
     is_magic(s)            
for l in v:
    for y in l:
        print(y, end = '')
    print(' ' , end = '')