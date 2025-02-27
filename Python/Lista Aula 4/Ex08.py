### Exercício 8
'''
Escreva um programa que leia três números reais e informe se eles constituem os lados de um triângulo.
Em caso afirmativo, informe se o triângulo é equilátero, isósceles ou escaleno. Para que três números
formem um triângulo deve ocorrer que a soma dos dois lados menores deve ser maior que o lado maior.
Para resolver essa questão será preciso usar os operadores and e or.
'''

A = float(input("digite o primeiro número real: "))
B = float(input("digite o segundo número real: "))
C = float(input("digite o terceiro número real: "))

if A + B > C and A + C > B and B + C > A:
    if A == B and A == C:
        print("Triângulo Equilátero")
    elif A == B or A == C or B == C:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")