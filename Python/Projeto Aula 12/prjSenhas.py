from random import randint, choice

### Função para gerar senhas
def GeraSenha(tipo, tamanho):
    esp = [43, 45, 95, 33, 63, 35, 64, 42, 38, 61, 36, 37] # Caracteres especiais em ASCII
    senha = ''
    match tipo:
        case 'A':
            for dig in range(tamanho):
                senha += chr(randint(48, 57))
        case 'B':
            for dig in range(tamanho):
                senha += chr(choice([randint(97, 122), randint(65, 90)]))
        case 'C':
            for dig in range(tamanho):
                senha += chr(choice([randint(48, 57), randint(65, 90)]))
        case 'D':
            for dig in range(tamanho):
                senha += chr(choice([randint(48, 57), randint(97, 122), randint(65, 90)]))
        case 'E':
            for dig in range(tamanho):
                senha += chr(choice([randint(48, 57), randint(97, 122), randint(65, 90), choice(esp)]))
    
    return senha

### Início do programa
valido = False
while valido == False:
    print('\nDigite o tipo de senha:')
    tipo = input('    >> ')

    if tipo == 'A' or tipo == 'B' or tipo == 'C' or tipo == 'D' or tipo == 'E':
        valido = True
    else:
        print('    Tipo de senha inválido')
        valido = False

print('\nDigite o tamanho da senha:')
tamanho = int(input('    >> '))

while tamanho < 6 or tamanho > 25:
    print('\nDigite um valor entre 6 e 25:')
    tamanho = int(input('    >> '))

### Leitura do Arquivo
with open('MATR.txt', 'r') as entrada:
    MATR = entrada.readlines()

### Saída
with open('SENHAS.txt', 'w') as saida:
    for i in range(len(MATR)):
        saida.write(f'{MATR[i].strip()};{GeraSenha(tipo, tamanho)};\n')