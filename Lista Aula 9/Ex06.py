### Exercício 6
'''
Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em
uma lista A somente se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste
intervalo devem ser ignorados. Ao final, apresentar a lista A e seu tamanho efetivo. Observe
que para este programa funcionar apropriadamente é necessário que LMin seja menor que LMax.
Caso o usuário digite LMax menor que LMin, o programa deve inverter os valores.
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

A = []
qtdA = 0
cont = 0
print('\nDigite 10 valores inteiros:')
while cont < 10:
    val = int(input('    >> '))
    if val <= LMax and val >= LMin:
        A.append(val)
        qtdA += 1
    cont +=1

print(f'\nLista A: {A}\nQuantidade de valores: {qtdA}')