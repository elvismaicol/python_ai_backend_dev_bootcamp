class Cachorro:
    # __init__ é um metodo inicializador da classe(ou contrutor)
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # __del__ é um metodo que destroi a instancia da classe(liberando a memoria ocupada)
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

# Com o del é possível forçar a execução do __del__ 
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()