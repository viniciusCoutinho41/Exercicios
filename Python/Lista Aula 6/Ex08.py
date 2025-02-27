### Exercício 8
'''
Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é
primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo.
'''

num = int(input("Digite um número: "))
divisao = 0
cont = 1
if num > 2:
    while cont != num+1:
        if num % cont == 0:
            divisao += 1
        cont += 1
    if divisao == 2:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")
elif num == 2:
        print(f"{num} é primo")
else:
        print(f"{num} não é primo")
