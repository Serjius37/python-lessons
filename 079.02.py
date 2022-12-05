''' Пирамида.
Вывести на экран пирамиду из чисел.
Входные данные:
Одно целое число NN.
Выходные данные:
Пирамида из натуральных чисел высоты NN.
Подсказки:
См. примеры входных и выходных данных. 
'''

#include <stdio.h>

int main() {
    int a;
    scanf ("%d", &a);
    for (int r = 1; r <= a; r++) {  
        for (int k = 1; k <= r; k++) {
            printf ("%d ", k);
        }
        printf ("\n");
    }    
    return 0;
}