with open ("multiplos de 4.txt","w") as multiplas4:
    with open("pares.txt") as pares:
        with open("impares.txt") as impares:
         for l in pares.readlines():
            if int(l) % 4 ==0:
                multiplas4.write(l)