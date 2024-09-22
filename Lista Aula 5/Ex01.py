### Exercício 1
'''
Escreva um programa que calcule os N primeiros termos de uma progressão geométrica (PG) com razão
R e primeiro termo P fornecidos pelo usuário. Também deve ser calculada e apresentada a soma desses
N termos.

Caso de teste:
Entrada: N = 8 P = 2 e R = 3
Saída: 2 6 18 54 162 486 1458 4374
'''

N = int(input("Digite o número de termos: "))
R = int(input("Digite a razão: "))
P = int(input("Digite o primeiro termo: "))
Soma = 0
Cont = 0

while(Cont < N):
    Soma = Soma + P
    print(P)
    P = P * R
    Cont += 1

print("Soma dos termos da PG:", Soma)