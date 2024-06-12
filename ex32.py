#ler 2 numeros e criar uma funcao para calcular a soma desses numeros

soma=0
sub=0
mult=0

def calcularsoma(n1,n2):
    soma = n1 + n2
    return soma

def calcularsub(n1,n2):
    sub = n1 - n2
    return sub

def calcuarmult(n1,n2):
    mult = n1 * n2
    return mult

def calculardiv(n1,n2):
    divi = n1/n2
    return divi

n1=int(input('n1: '))
n2=int(input('n2: '))
soma=calcularsoma(n1,n2)
sub=calcularsub(n1,n2)
mult=calcularmult(n1,n2)
divi=calculardiv(n1,n2)
print(soma,sub,mult,divi)