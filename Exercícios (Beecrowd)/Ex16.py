### Exercício 16 (Beecrowd - 1099)
'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y.
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
    A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
    Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
    Imprima a soma de todos valores ímpares entre X e Y.
'''

N = int(input())
cont = 0
somaImp = 0

while cont < N:
    X, Y = map(int, input().split())
    if X < Y:
        X += 1
        while X < Y:
            if X % 2 != 0:
                somaImp += X
            X += 1
    else:
        X -= 1
        while X > Y:
            if X % 2 != 0:
                somaImp += X
            X -= 1
    print(somaImp)
    somaImp = 0
    cont += 1