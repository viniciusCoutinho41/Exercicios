### Exercício 10
'''
Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.
'''

num = int(input("Digite o número de termos: "))
while  num <= 0:
    num = int(input("Digite um número maior que zero: "))
    
Prim = int(input("Digite o valor de Prim: "))
cont = 0
n1 = 0
n2 = 1
n3 = 0

while num > cont:
    if n1 > Prim:
        print(n1)
        cont += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3