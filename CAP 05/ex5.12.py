# Mesmo programa  o valor que será depositado mensalmente. Esse valor
#  será depositado no inicio de cada mês, e você deve calcular o juros
#     a cada mês
x=1
soma = 0
while x <= 5:
    n = int (input(f"{x} Digite um  valor para depositado: "))
    soma = soma + n 
    x = x + 1

    print(f"Valor: {soma / 5:5.2f} de juros na poupança")
