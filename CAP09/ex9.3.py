#criação de numeros impares e pares em um so

with open ("impares.txt","w") as imparespares:
        for n in range(0,1000):
            if n%2==0:
                imparespares.write(f"{n}\n")
          