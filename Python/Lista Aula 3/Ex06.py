### Exercício 6
'''
Escreva a sequência de comandos para calcular o salário bruto de um profissional que ganha por hora,
sabendo que ele ganha R$ 14,25/h e trabalhou 163 horas normais e 20 horas extras (pagam o dobro).
'''

salHora = 14.25
tempo = 163
extra = 20
bruto = ((salHora * tempo) + (2 * salHora * extra))
print(bruto)