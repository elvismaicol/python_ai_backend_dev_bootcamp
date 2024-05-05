from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


class Cliente: 
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_trasacao(self, conta, trasacao):
        trasacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    # mapeando classmetodo nova_conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    # mapeando os medoto para acessar o atributo privado saldo
    @property
    def saldo(self):
        return self._saldo

    # mapeando os medoto para acessar o atributo privado numero da conta
    @property
    def numero(self):
        return self._numero

    # mapeando os medoto para acessar o atributo privado agencia
    @property
    def agencia(self):
        return self._agencia

    # mapeando os medoto para acessar o atributo privado cliente
    @property
    def cliente(self):
        return self._cliente   

    # mapeando os medoto para acessar o atributo privado histórico
    @property
    def historico(self):
        return self._historico   

    def sacar(self, valor):
        self.saldo = saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n!!! Operação falhou! Você não tem saldo suficiente. !!!")

        elif valor > 0:
            print("\n@@@ Saque realizado com sucesso! @@@")
            return True
        
        else:
            print("\n!!! Operação falhou! O valor informado é inválido. !!!")
 
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n@@@ Depósito realizado com sucesso! @@@")
        else:
            print("\n!!! Operação falhou! O valor informado é inválido. !!!")
            return False

        return True
    

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    # Sobrescrevendo o metodo de saque para fazer validações
    def sacar(self, valor):
        numero_saques = len(
            # compressão de listas
            [
                transacao for transacao in self.historico.transacao 
                    if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n!!! Operação falhou! O valor do saque excede o limite. !!!")

        elif excedeu_saques:
            print("\n!!! Operação falhou! Número máximo de saques excedido. !!!")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacoes(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }

        )

# Criando a classe abstrata Transacao
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# mapeando saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacoes(self)


# mapeando deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacoes(self)
