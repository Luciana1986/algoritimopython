# escrever um programa em python que leia um vetor v1 de n posições e gere um vetor
#v2 de tamanho n que é o vetor v1 invertido

import random
#criar o vetor

tam = int(input('digite o tamanho:'))
v1 = [0] * tam
v2 = [0] * tam
#preencher o primeiro vetor

for i in range(tam):
    v1[i] = random.randint(0,9)

for i in range(tam):
    v2[tam - 1 - i] = v1[i]

print (v1, v2)