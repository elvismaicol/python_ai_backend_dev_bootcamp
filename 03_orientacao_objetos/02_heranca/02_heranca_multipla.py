class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

# Mixin => possibilita adicionar comportamento para classe
class FalarMixin:
    def falar(self):
        return "Estou falando"


class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # mro => metodos que possibilitam ver a ordem da resolução que o interpretador python vai utilizar para encontrar
        # os atributos e os metodos dentro da classe
        #print(Ornitorrinco.__mro__)
        #print(Ornitorrinco.mro())
        
        super().__init__(
            cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas
            ) 

#gato = Gato(2, "preto")
# quando usado **kw é preciso passar os argumentos com chave valor
gato = Gato(nro_patas=2, cor_pelo="preto")
print(gato)

print("=" * 20)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="vermelho", cor_bico="marrom")

print(ornitorrinco)
print(ornitorrinco.falar())