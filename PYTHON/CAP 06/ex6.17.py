# CRIAÇÃO DE PROGRAMA DE ESTOQUE DE SUPERMERCADO 
tabela= {
          "cigarro":[10,1.00],
          "whiskey":[10,2.00],
          "agua":[10,3.00],
          "leite":[10,4.00],
}

produto= input(f"Digite o produto que você quer da {tabela}:  ")
quantidade= int (input("Digite a quantidade desejada? "))

venda = produto, quantidade
total = 0
for operação in venda:

    preço = tabela [produto][1]
    custo = preço*quantidade
    print(f"{produto:12s}:{quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    tabela[produto][0] -= quantidade
    total += custo
    print(f"custo total:{total:21.2f}\n")
    print("estoque:\n")
    for chave, dados in tabela.items():
        print("descrição  ", chave)
        print("quantidade: ",dados[0])
        print(f"preço:{dados[1]:6.2f}\n")