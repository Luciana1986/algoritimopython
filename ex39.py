#faça um programa que leia um vetor A com 4 numeros inteiros, calcule e mostre a soma dos quadrado dos
#elementos do vetor.

somaquadrados = 0
for i in range(4):
    somaquadrados +=int(input(f"{i+1}° numero:"))**2
print(f"soma dos quadrados {somaquadrados}")