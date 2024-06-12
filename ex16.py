#elabore um programa que leia 10 númers e mostre a soma
x=1
soma=0
while x<=10:
    num = int(input('numero:'))
    soma = soma + num
    x=x+1
print('soma:',soma)
