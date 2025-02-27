### Exercício 7 (Beecrowd - 1072)
'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
mostrando essas informações.

Entrada
    A primeira linha da entrada contém um valor inteiro N (N < 10000),
    que indica o número de casos de teste.
    Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
    Para cada caso, imprima quantos números estão dentro (in)
    e quantos valores estão fora (out) do intervalo.
'''

N = int(input())
cont = 0
dentro = 0
fora = 0
while cont < N:
    X = int(input())
    if X >= 10 and X <= 20:
        dentro += 1
    else:
        fora += 1
    cont+=1
    
print(f'{dentro} in')
print(f'{fora} out')