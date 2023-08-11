# programa de tentativa e erro
import random
n = random.randint(1,10)
x = int(input("escolha um numero entre 1 a 10: "))
if x ==n:
    print("win")
if x != n:
    print("2 tentativa")
    x = int(input("Tente novamente numero de 1 a 10: "))
if x != n:
    print("3 tentativa")
    x = int(input("Tente novamente numero de 1 a 10: "))

else: 
    print("lose")