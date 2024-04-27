# Como iterar sobre itens de um dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# Forma mais indicada(usar items() que retorna uma lista 
# de tupla, 1º elemento é a chave e 2º o valor)
for chave, valor in contatos.items():
    print(chave, valor)