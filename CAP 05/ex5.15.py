# Programa para controlar uma pequena maquina registradora. Você
#  solicitar ao usario que digite o codigo do produto e a quantidade
#     comprada.Utilize a tabela de codigos para acessar os preços de cada produto

# CODIGO     PREÇO R$:
#   1           0,50
#   2           1,00
#   3           4,00
#   5           7,00
#   9           8,00


codigo = int (input("Digite um codigo do produto para saber o preço ou 0 para sair:  "))


while True:
  if codigo == 1:
   print(0.50)
  if codigo == 2:
   print(1.00)
   if codigo == 3:
    print(4.00)
    if codigo == 5:
     print(7.00)
    if codigo == 9:
     print(8.00)
    if codigo == 0:
      break

      



