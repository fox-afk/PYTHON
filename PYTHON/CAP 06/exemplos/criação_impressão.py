compras = []
while True:
    produto = input("produto: ")
    if produto =="fim":
        break
    quantidade = int (input("quantidade: "))
    preço = float(input("preço:"))
    compras.append([produto,quantidade,preço])
    soma= 0.0
    for e in compras:
        print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}")
        soma += e[1] * e[2]
        print(f"TOTAL:{soma:7.2f}")