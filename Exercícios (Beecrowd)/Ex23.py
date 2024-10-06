### Exercício 23 (Beecrowd - 1144)
'''
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas
na execução do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos,
todos os dígitos devem ser apresentados.

Entrada
    O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

Saída
    Imprima a saída conforme o exemplo fornecido.
'''

N = int(input())
cont = 0
val1 = 1
while cont < N:
    val2 = val1 * val1
    val3 = val2 * val1
    print(f'{val1} {val2} {val3}')
    print(f'{val1} {val2+1} {val3+1}')
    val1 += 1
    cont += 1