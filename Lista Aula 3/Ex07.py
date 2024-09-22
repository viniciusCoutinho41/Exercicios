### Exercício 7
'''
Escreva em Python as seguintes expressões aritméticas e teste-as para os valores A = 4, B = 5, C = 1
𝑅 = (𝐴 + 𝐵)/2

𝑅 = ((3𝐴 + 2𝐵)/(𝐴 + 𝐵))

𝑥 = −𝐵 + √(𝐵2 − 4𝐴𝐶)/2𝐴
𝑍 = 7.6𝐴 − 𝐵 ** 1,7
'''

import math
A = 4
B = 5
C = 1

R = (A + B)/2
print(R)

R = ((3 * A + 2 * B)/(A + B))
print(R)

X = (-B + (math.sqrt((B ** 2) - 4 * A * C)))/ (2 * A)
print(X)

Z = 7.6 * A - B ** 1.7
print(Z)