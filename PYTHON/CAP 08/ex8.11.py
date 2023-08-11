# Função recebe como parametro a string, o numero minimo e maximo de caracteres
#  Retorne verdadeiro se o tamanho da string estiver entre os valores de 
#  maximo e minimo e falso

def parametro(tamanho,minimo,maximo):
    while True:
        v = int (input(tamanho))
        if  v < minimo or v > maximo:
            print(f"string pequena. {minimo} ou {maximo}")
        else:
            return v 