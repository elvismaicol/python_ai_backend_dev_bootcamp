
from abc import ABC, abstractmethod, abstractproperty

# informando que a class ControleRemoto extende de ABC
class ControleRemoto(ABC):
    # tranformando metodo em abstrato
    @abstractmethod
    def ligar(self): # contrato
        pass

    @abstractmethod
    def desligar(self): # contrato
        pass

    # Forçando uma propriedade, obrigatoriedade de ser implementado
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV ...")
        print("Ligada!")
    
    def desligar(self):
        print("Desligando a TV ...")
        print("Desligada!")

    @property
    def marca(self):
        return "Sansung"


# *Vai dar erro porque não foi implementado o metodo abstrato "desligar"
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando a Ar...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a Ar ...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

# erro*:
controle_ar = ControleArCondicionado()
controle_ar.ligar()
print(controle_ar.marca)