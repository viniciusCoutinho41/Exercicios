### Exercício 2
'''
Escreva um programa que leia valores numéricos inteiros e totalize (totalizar é somar todos os números)
separadamente os positivos e os negativos até que o usuário digite 0. Ao final mostre na tela esses dois
totais.

Caso de teste:
Entrada: 12 -3 5 1 -4 -9 6 0
Saída: Total dos positivos = 24
Total dos negativos = -16
'''

num = 1
SomaP = 0
SomaN = 0

while num != 0:
    num = int(input("Digite um número diferente de zero: "))
    if num > 0:
        SomaP += num
    elif num < 0:
        SomaN += num

print("Soma números positivos:", SomaP)
print("Soma números negativos:", SomaN)