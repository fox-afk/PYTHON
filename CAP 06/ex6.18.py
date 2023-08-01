palavra = input("Digite uma palavra:  ")
a = {}
for letra in palavra:
    if letra in a:
        a[letra] = palavra[letra] + 1
    else:
        a[letra] =1
print(a)