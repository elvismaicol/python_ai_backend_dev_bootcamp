class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        pass

conta = Conta(100)
conta.depositar(100)

# forma incorreta de acessar o atributo
print(conta._saldo)