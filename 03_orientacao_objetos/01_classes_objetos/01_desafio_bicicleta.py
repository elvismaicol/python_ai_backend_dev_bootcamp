# criando uma classe
class Bicicleta:
    #inicialisando os atributos da classe com metodo construtor
    # self: referencia ao objeto
    def __init__(self, cor, modelo, ano, valor):
        #atributos da classe
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor 
    
    #metodo buzinar
    def buzinar(self):
        print("Plim Plim ....")

    #metodo parar
    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada!")
    
    #metodo correr
    def correr(self):
        print("Vrummm ...")
    
    #def __str__(self):
    #    return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
   

b1 = Bicicleta("azul", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 1200)
Bicicleta.buzinar(b2)

print(b2)
