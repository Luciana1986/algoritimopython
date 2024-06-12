#Elabore uma função que digitados 3 números mostre o maior número

maior=0
def obtermaior(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        maior = n1
    elif (n2 > n1) and (n2 > n3):
        maior = n2
    else:
        maior = n3
    return maior

n1 = int(input("N1:"))
n2 = int(input("N2:"))
n3 = int(input("N3:"))
maior = obtermaior(n1, n2, n3)
print(maior)