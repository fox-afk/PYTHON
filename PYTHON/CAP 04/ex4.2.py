# Programa de velocidade e multa(velocidade x 5)

velocidade= int ( input("digite a velocidade do  automovel ?"))
calculo= velocidade *5
passou =80
if velocidade <= 80:
    print("Não vai pagar multa")
if velocidade > 80:
    print(f"Vai pagar a multa valor R$:{calculo}")