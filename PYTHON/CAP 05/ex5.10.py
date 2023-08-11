# modifique o programa anterior para que aceite 
#   respostas com letras maiusculas e minusculas em todas as questões


pontos = 0
questão= 1

while questão<=3:
    resposta = input (f"Respostas da questão {questão}: ")
    if questão ==  1 and resposta == "b":
        pontos = pontos + 1
    if questão == 2 and resposta =="a":
         pontos = pontos + 1
    if questão == 3 and resposta =="d":
        pontos = pontos + 1
        questão = questão + 1
        print(f"O aluno fez {pontos} pontos(s)")