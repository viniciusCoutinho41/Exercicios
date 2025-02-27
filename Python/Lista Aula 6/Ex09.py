### Exercício 9
'''
Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
0 e 1.

Caso de Teste: se N = 9 então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21
'''

num = int(input("Digite o número de termos: "))
while  num < 1:
    num = int(input("Digite um número maior que zero: "))
    
cont = 0
n1 = 0
n2 = 1
n3 = 0

while cont < num:
    print(n1)
    cont += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3