'''
Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает nn различных последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и строчного латинского алфавита, при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
Формат входных данных
В первой строке подаётся число nn – количество сообщений, в последующих nn строках вводятся строки, содержащие латинские строчные буквы и цифры.
Формат выходных данных
Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
Примечание: Числа 11 необязательно должны быть разделены другими символами, нужно подсчитать вхождение последовательности символов "11", т.е. например в строке "111" содержится одна такая последовательность, в то время как в "1111" их уже две.
'''

v = int(input()) 
k = 0
for i in range (v):
    s = input() 
    if s.count('11') >= 3 :
        k += 1
print(k) 