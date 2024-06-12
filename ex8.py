n1=float(input('nota1:'))
n2=float(input('nota2:'))
md=(n1+n2)/2
if md>=7:
    print('aprovado')
elif md<5:
    print('reprovado')
elif (md>=5 and md<7):
    print('recuperação')