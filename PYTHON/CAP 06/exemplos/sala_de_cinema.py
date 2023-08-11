lugares_vagos = [ 10,2,1,3,0]
while True:
   sala = int (input("sala (0 sai):  "))
   if sala == 0:
        print('fim')
        break
   if sala > len(lugares_vagos) or sala < 1:
        print("sala invalida")
   elif lugares_vagos[sala -1] ==0:
        print("desculpe, sala lotada!")
   else:
     lugares= int(input(f"Quantas lugares ({lugares_vagos [sala -1]} vagos): "))
if lugares > lugares_vagos[sala -1]:
       print("esse numero de lugares não está disponivel")
elif lugares<0:
     print("numero invalido")
else:
     lugares_vagos[sala -1] -= lugares
     print(f"{lugares} lugares vendidos ")
     print("utilização das salas")
     for x,l in enumerate(lugares_vagos):
          print(f"Sala {x+1} -{l} lugar(es) vazios(s)")