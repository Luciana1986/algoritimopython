n = 1
somaidade = 0
mediaidade = 0
maisvelho = 0
nomemaisvelho =''
nomemaisnovo =''
maisnovo=140
while n <= 5:
    nome = input('nome:')
    idade = int(input('idade:'))
    if idade>maisvelho:
        nomemaisvelho=nome
        maisvelho=idade
    if idade<maisnovo:
        nomemaisnovo=nome
        maisnovo=idade
    somaidade =somaidade+idade
    n = n + 1
mediaidade = somaidade/5
print('mais velho:', nomemaisvelho)
print('idade mais velho:', maisvelho)
print('mais novo:', nomemaisnovo)
print('idade maisnovo:', maisnovo)
print('soma idades:', somaidade)
print('media idades', mediaidade)




