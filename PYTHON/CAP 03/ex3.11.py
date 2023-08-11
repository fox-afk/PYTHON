# CAIXA DE SUPERMECADO

produto = input("Digite o produto:   ")
preço = float (input(f"Digite o preço do {produto}"))
desconto = 20

if preço >= 50.00:
    calculo= preço * ( desconto/ 100)


print(produto)
print(f"R$:{calculo}")