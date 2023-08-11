# programa que pergunte o salario do funcionario e calcule o aumento. Salario superior a R$:1.250,000, 
#   calcule um aumento de 10%. para inferiores ou iguais , de 15%

salario= float (input("digite o salario:     "))

if salario > 1250:
 valor = salario + (salario * 0.10)

if salario <= 1250:
  valor = salario + (salario * 0.15)
print(f'O seu novo salario é {valor}')