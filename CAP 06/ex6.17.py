estoque = { "tomate":  [100  ,2.30],
            "alface":  [100  ,0.45],
            "batata":  [100  ,1.20],
            "feijão":  [100  ,1.50]}
venda= [["tomate",5], ["batata",10],["alface",5]]
total= 0
print("vendas:\n")
for operação in venda:
    produto, quantidade = operação
    preço =  estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo

print(f"Custo total: {total:21.2f}\n")
print("estoque:\n")
for chave, dados  in estoque.items():
    print("descrição: ", chave)
    print("quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")