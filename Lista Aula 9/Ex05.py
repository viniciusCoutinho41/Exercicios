### Exercício 5
'''
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir
isso em um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os
valores lidos em A em outras duas listas NEG e POS, a primeira contendo somente os valores negativos
e a segunda contendo os valores positivos e zero. Apresentar na tela as listas NEG e POS e a
quantidade de valores contidos em cada uma.
'''

print('Digite um valor entre 0 e 50')
N = int(int(input('    >> ')))

while N < 0 or N > 50:
    print('    Valor inválido')
    N = int(int(input('    >> ')))

cont = 0
A = []
print(f'\nDigite {N} valores para a lista A:')
while cont < N:
    A.append(float(input('    >> ')))
    cont += 1

NEG = []
POS = []
qtdNEG = 0
qtdPOS = 0
for item in A:
    if item > 0:
        POS.append(item)
        qtdPOS += 1
    elif item < 0:
        NEG.append(item)
        qtdNEG += 1

print(f'Números negativos: {NEG}\nQuantidade de negativos: {qtdNEG}')
print(f'\nNúmeros positivos: {POS}\nQuantidade de positivos: {qtdPOS}')