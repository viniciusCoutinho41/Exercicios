### Exercício 1
'''
Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
para esse número fornecido. Siga o formato apresentado abaixo (supondo que foi digitado 4):
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40
'''

num = int(input('Digite um número inteiro: '))
cont = 1

while cont <= 10:
    print(f'{num} x {cont} = {num * cont}')
    cont+=1