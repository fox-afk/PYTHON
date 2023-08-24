# PROGRAMA DE FILAS COM 2 FILAS. 

# COMANDO "A" PARA ATENDIMENTO DA FILA 1, E "B" PARA ATENDIMENTO DA FILA 2. 
#CONSIDERE A CHEGADA DE CLIENTES: "F" PARA FILA 1 E "G" PARA FILA 2

ultimo = 10
fila = list (range(1,ultimo +1))
while True:
    print(f"\nExistem/{len(fila)} clientes na fila ")
    print(f"fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("ou A para atendimento, ou 0 para sair ")
    operacao = input("Operação (F A OU 0):  ")
    if operacao =="A":
        if len(fila >0):
            atendido = fila.pop(0)
            print(f"cliente {atendido} atendido")
        else:
            print("Fila vazia!")
    elif operacao=="B":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == 0:
        break
    else:
        print("Operação invalida!")