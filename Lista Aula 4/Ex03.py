### Exercício 3
'''
Escreva um programa que leia dois números quaisquer e mostre na tela qual é o menor e qual é o maior.
'''

n1 = float(input("digite um número: "))
n2 = float(input("digite um número: "))

if n1 < n2:
    print(f"{n1:.2f} é o menor número\n{n2:.2f} é o maior número")
elif n1 > n2:
    print(f"{n2:.2f} é o menor número\n{n1:.2f} é o maior número")
else:
    print("ambos são iguais")