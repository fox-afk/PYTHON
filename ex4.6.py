# um programa que pergunte a distancia que um passageiro deseja percorrer em km.Calcule o preço da passagem
# cobrando  R$: 0,50 por km para viagem de até de 200 km , e de R$:0,45 para viagens mais longas.


cobrança = int (input("Qual a distancia sera percorrida?")) 

if cobrança <= 200:
  valor =( cobrança + (cobrança * 0.50) )

  print(f"O valor a ser cobrado é R$:{valor}")
  
if cobrança > 200:
  outrovalor =  ( cobrança + (cobrança * 0.45   ))

  print(f"O valor a ser cobrado é R$:{outrovalor}")
