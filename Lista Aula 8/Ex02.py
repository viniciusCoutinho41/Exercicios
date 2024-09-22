### Exercício 2
'''
Refaça o programa anterior, porém ao final exiba na tela cada elemento da lista em uma linha da tela
(este programa deve exibir um elemento por vez dentro de um laço e usando um índice para acessar
cada elemento individualmente).
'''

print('Digite um valor positivo (zero ou negativo para sair)')
num = float(input('   >> '))
lista = []

while num > 0:
    lista.append(num)
    num = float(input('   >> '))

print('\nValores digitados:')
for i in lista:
    print(i)