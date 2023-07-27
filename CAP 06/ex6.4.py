ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print(f"\nExistem{len(fila)} clientes na fila")
    print(f"Fila atual:{fila}")
    print("Digite F para adicionar um cliente na fila,")
    print("ou A para realizar. S para sair")
    operação = input("Operação:(F, A OU S):")
    if operação =="A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("fila vazia! ninguem para atender")
    elif operação =="F":
        ultimo += 1 
        fila.append(ultimo)
    elif operação =="S":
        break
    else:
        print("operação realizada! digite apenas F , A ou S !")
