### Exercício 7
'''
Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado,
onde N é um número fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho
fixo de 10 sugerido no programa anterior
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
qtdA = 0
cont = 0
print(f'\nDigite {N} valores inteiros:')
while cont < N:
    val = int(input('    >> '))
    if val <= LMax and val >= LMin:
        A.append(val)
        qtdA += 1
    cont +=1

print(f'\nLista A: {A}\nQuantidade de valores: {qtdA}')