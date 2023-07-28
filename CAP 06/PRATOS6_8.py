# PILHA DE PRATOS


prato = 5
pilha = list(range(1,prato +1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"pilha atual:{pilha}")
    print("Digite E para empilhar um novo prato")
    print("ou D para desempilhar, S para sair")
    operacacao = input("Operação (E , D ou S): ")
    if operacacao == "D":
      if len(pilha) > 0:
         lavado = pilha.pop(-1)
         print(f"prato {lavado} lavado")
      else:
        print("pilha vazia !")
    elif operacacao =="E":
       prato += 1
       pilha.append(prato)
    elif operacacao =="S":
       break
    else:
       print("operação invalida! digite E , D ou S")
