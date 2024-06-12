a=float(input('digite a medida'))
b=float(input('digite a medida'))
c=float(input('digite a medida'))

if (a==b and b==c and a==c):
    print('equilatero')
elif (a==b and b==c or a==c):
    print('isosceles')
elif (a!=b and b!=c and a!=c):
    print('escaleno')