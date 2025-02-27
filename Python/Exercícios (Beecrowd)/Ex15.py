### Exercício 15 (Beecrowd - 1035)
'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo
o esquema abaixo, da esquerda para a direita. 
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal
segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

tipo1 = input()
tipo2 = input()
tipo3 = input()
animal = ''

if tipo1 == 'vertebrado':
    if tipo2 == 'ave':
        if tipo3 == 'carnivoro':
            animal = 'aguia'
        elif tipo3 == 'onivoro':
            animal = 'pomba'
    elif tipo2 == 'mamifero':
        if tipo3 == 'onivoro':
            animal = 'homem'
        elif tipo3 == 'herbivoro':
            animal = 'vaca'

elif tipo1 == 'invertebrado':
    if tipo2 == 'inseto':
        if tipo3 == 'hematofago':
            animal = 'pulga'
        elif tipo3 == 'herbivoro':
            animal = 'lagarta'
    elif tipo2 == 'anelideo':
        if tipo3 == 'hematofago':
            animal = 'sanguessuga'
        elif tipo3 == 'onivoro':
            animal = 'minhoca'

print(animal)