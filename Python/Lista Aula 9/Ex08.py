### Exercício 8
'''
Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do
intervalo [Min, Max] sejam inseridos em uma segunda lista chamada R. Apresentar na tela a
lista de valores aceitos (lista A) e a lista de valores rejeitados (lista R),
bem como o tamanho de cada um.
'''

print('Digite o valor de LMin:')
LMin = int(input('    >> '))

print('\nDigite o valor de LMax:')
LMax = int(input('    >> '))

aux = 0
if LMin > LMax:
    aux = LMin
    LMin = LMax
    LMax = aux

print('\nDigite a quantidade de valores a serem lidos:')
N = int(input('    >> '))

A = []
R = []
qtdA = 0
qtdR = 0
cont = 0
print(f'\nDigite {N} valores inteiros:')
while cont < N:
    val = int(input('    >> '))
    if val <= LMax and val >= LMin:
        A.append(val)
        qtdA += 1
    else:
        R.append(val)
        qtdR += 1

    cont +=1

print(f'\nLista de valores aceitos (lista A): {A}\nQuantidade de valores: {qtdA}')
print(f'\nLista de valores rejeitados (lista R): {R}\nQuantidade de valores: {qtdR}')