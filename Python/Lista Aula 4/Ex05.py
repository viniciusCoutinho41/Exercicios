### Exercício 5
'''
Escreva um programa que leia um número inteiro e informe se o mesmo é positivo, zero ou negativo.
'''

num = int(input("digite um número inteiro: "))

if num > 0:
    print(f"{num} é um número positivo")
elif num < 0:
    print(f"{num} é um número negativo")
else:
    print("o número que foi digitado é zero")