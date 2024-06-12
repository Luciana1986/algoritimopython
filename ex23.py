#elabore um programa ue leia nome, idade,mostre a soma das idades,medias das idades de 10 pessoas

n = 1
somaidade = 0
mediaidade = 0
while n <= 10:
    nome = input('nome:')
    idade = int(input('idade:'))
    somaidade = somaidade + idade

    n=n+1
mediaidade = somaidade/10
print('soma idades:',somaidade)
print('media idades:'/mediaidade)