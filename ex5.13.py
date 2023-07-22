# Escreva um programa que pergunte o valor inicial de 
#  uma divida e o juro mensal. Pergunte o valor mensal que será pago
#     Mostre o numero de meses para que a divida seja paga, 
#         o total e o total de juros pago.

valor = int (input ("Digite o valor inicial  R$:   "))
falsojuros = int (input ("Digite o valor do juros R$:   "))
data = int (input("Digite se será mensal, semestral ou anual:"))

juros = falsojuros / 100

calculo =  (data *(valor * juros))

print(f'O valor com juros é {calculo}, e sem juros é {valor}')

