# escreva um programa que pergunte o deposito inicial
#   e a taxa de juros de uma poupança. Exiba os valores 
#   mês a mês para os 24 primeiros meses. Escreva o total
#     ganho com juros no periodo.

x=1
soma = 0
while x <= 5:
    n = int (input(f"{x} Digite um  valor para depositado: "))
    soma = soma + n 
    x = x + 1

    print(f"Valor: {soma *5:5.2f} com juros na poupança")