class Conta: 
    def __init__(self, clientes,numero,saldo=0):
        self.saldo= saldo
        self.clientes=clientes
        self.numero=numero
    def resumo (self):
        print(f"cc numero: {self.numero} saldo: {self.saldo:10.2f}")
    def saque (self,valor):
        if self.saldo>=valor:
            self.saldo -= valor
    def deposito(self,valor):
        self.saldo+= valor