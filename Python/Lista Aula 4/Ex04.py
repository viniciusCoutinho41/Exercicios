### Exercício 4
'''
Escreva um programa que leia um número inteiro e apresente na tela se ele é par ou ímpar (para
determinar se um número é par ou ímpar verifique se o resto da divisão dele por 2 é zero ou não. Para
isso use o operador % para calcular esse resto).
'''

num = int(input("digite um número inteiro: "))

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é impar")