# adiciona um elemento ao conjunte se o elemento ainda não existir

sorteio = {1, 23}

sorteio.add(25)  
print(sorteio)
# {1, 23, 25}

sorteio.add(42)  
print(sorteio)
# {1, 23, 25, 42}

sorteio.add(25)  
print(sorteio)
# {1, 23, 25, 42}