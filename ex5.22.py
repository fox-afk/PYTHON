x = input("escolha a operação matematica(*,+,- e / ):  ")


tabuada = 1 
numero = 1
while numero <= 10:
         print(f"{tabuada} x {numero} = {tabuada * numero}")
numero += 1
if numero == 11:
        numero = 1
tabuada += 1