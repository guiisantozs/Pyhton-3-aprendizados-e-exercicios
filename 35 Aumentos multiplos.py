salario = float(input('Qual é o seu salário? R$'))
if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print('O seu salario com reajuste será de R${:.2f}'.format(salario))