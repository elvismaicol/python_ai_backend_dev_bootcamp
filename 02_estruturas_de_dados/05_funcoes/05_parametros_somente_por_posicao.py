# Exemplo de função com parametros aceitos apenas por posição, a "/" delimita até onde os paramentos são por posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
# TypeError: criar_carro() got some positional-only arguments passed as keyword arguments: 'modelo, ano, placa'