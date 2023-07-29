# pesquisa sequencial

L = [15,7,27,39]
p = int (input("Digite o valor a procurar:  v"))
x = 0
while x < len(L):
    if L[x] == p:
        break
    else:
        print(f"{p} não encontrado")