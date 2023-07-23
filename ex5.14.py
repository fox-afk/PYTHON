# programa que leia numeris inteiros do teclado. O programa
#   deve ler os numeros até que o usuario digite 0(zero). No
#      final da execução, exiba a quantidade de numeros  digitados
#         assim como a soma e a medida aritmetica

s = 0 
while True:
    v= int (input("digite um numero a somar ou 0 para sair:   "))
    if v == 0:
        break
    s += v

    print(s)