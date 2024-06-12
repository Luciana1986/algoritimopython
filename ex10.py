# CALCULE UM PROGRAMA QUE LEIA O SALÃRIO E CALCULE O AUMENTO, O AUMENTO SERÁ DE 5% PARA SALARIOS >2500
#AUMENTO DE 7% PARA SALARIO <=2500

salario=float(input('salario:'))

if salario>2500:
    aumento = salario * 0.05
elif salario<=2500 :
    aumento = salario * 0.07

novosalario = salario+aumento
print('salario:',salario)
print('aumento:',aumento)
print('novo salario;',novosalario)