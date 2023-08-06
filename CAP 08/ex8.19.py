import entrada
L = []
for x in range(10):
    L.append(entrada.valida_inteiro("digite um numero,0,20"))
    print(f"soma:{sum(L)}")