#conta com registro de operações e extrato (contas.py)

class Conta:
    def __init__(self,clientes,numero,saldo=0):
        self.saldo=0
        self.clientes=clientes
        self.numero= numero
        self.operações=[]
        self.deposito(saldo)
    def resumo(self):
        print(f"CC Numero {self.numero} Saldo: {self.saldo:10.2f}")
    def saque(self, valor):
        if self.saldo>=valor:
            self.saldo-=valor
            self.operações.append(["saque",valor])
    def deposito(self,valor):
        self.saldo+= valor
        self.operações.append(["deposito",valor])
    def extrato(self):
        print(f"extrato CC numero{self.numero}\n")
        for o in self.operações:
            print(f"{o[0]:10s}  {o[1]:10.2f}")