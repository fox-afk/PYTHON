 # leitor de notas

valor = int (input("Digite o valor a pagar: "))
cedulas = 0
atual= 50
apagar= valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cedula(s) de R$:{atual}")
        if apagar == 0:
            break
        if atual == 100 :
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0