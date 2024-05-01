# Para percorrer um SET podemos iterar dentro de um FOR

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#enumerate ver o indice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")