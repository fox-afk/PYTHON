# Programa que aprove imprestimo bancario para comprar uma casa. O programa deve perguntar o valor da casa a comprar
#   o salario e a quantidade de anos a pagar. o valor da prestação mensal não pode ser superior a 30% do salario.
#     Calcule a prestação como sendo o valor da casa a comprar divido pelo numero de meses a pagar


casa    = float (input("Qual o valor da casa? R$: "))
salario = float (input("Qual e o seu salario  R$: "))
anos = int (input("Quantos anos demora para pagar a casa?"))

valo_casa= casa / anos 


print(f'O valor da casa é de R$:{casa}')
print(f'o salario é de R$:{salario}')
print(f'demora {anos} anos')
print(f'{valo_casa} por ano')