salario = float(input('salario:'))
reajuste = float(input('reajuste:'))
reajuste = salario * (reajuste/100)
novosalario = salario+reajuste
print('salario:',salario)
print('reajuste:',reajuste)
print('novo salario:',novosalario)