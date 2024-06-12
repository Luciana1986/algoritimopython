a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

if (a<b+c) and (a>b-c):
    print('triangulo')
if (a==b) and (b==c):
    print('equilatero')
elif (a==b) or (b==C) or (a==c):
    print('isosceles')
elif (a!=b) and (b!=a) and (a!=c):
    print('escaleno')
else:
    print('não e um triangulo')

