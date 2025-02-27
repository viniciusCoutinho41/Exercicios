### Exercício 9 (Beecrowd - 1080)
'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
    O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
    Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

cont = 0
pos = 0
maior = 0

while cont < 100:
    num = int(input())

    if num > maior:
        maior = num
        pos = cont + 1
    cont += 1

print(maior)
print(pos)