###Exercício 4
'''
Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida
o programa deve juntar as duas listas em uma única com o tamanho 20.
'''

print('Digite 10 valores para a primeira lista')
lista1 = []
lista2 = []
listaFinal = []
cont = 0

while cont < 10:
    num = int(input('   >> '))
    lista1.append(num)
    cont += 1
cont = 0

print('\nDigite 10 valores para a segunda lista')
while cont < 10:
    num = int(input('   >> '))
    lista2.append(num)
    cont += 1

listaFinal = lista1 + lista2
print(f'\nSoma das duas listas:\n{listaFinal}')