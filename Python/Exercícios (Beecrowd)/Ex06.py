### Exercício 6 (Beecrowd - 1071)
'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
    O arquivo de entrada contém dois valores inteiros.

Saída
    O programa deve imprimir um valor inteiro.
    Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada
    que deverá caber em um inteiro.
'''

X = int(input())
Y = int(input())
aux = 0
somaImpar = 0

if X > Y:
    aux = X
    X = Y
    Y = aux
cont = X + 1

while cont < Y:
    if cont % 2 != 0:
        somaImpar += cont
    cont += 1
    
print(somaImpar)