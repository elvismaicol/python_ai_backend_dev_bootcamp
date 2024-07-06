from typing import List

class MeuIterador:
    #def __init__(self, numeros: list[int]): #versão do python superior a 3.9
    def __init__(self, numeros: List[int]): # usado List[int] devido a versão do python 3.8
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)