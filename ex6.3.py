# apresentação de numeros

numeros = [0,0,0,0,0]
x = 0
while x < 5:
    numeros[x] = int (input(f'Numero {x + 1}: '))
    x+=1
    while True:
        escolhido = int (input("Que posição você quer que monstre( 0 para sair):  "))
        if escolhido==0:
            break
        print(f"Você escolheu o numero:  {numeros[escolhido-1]}")