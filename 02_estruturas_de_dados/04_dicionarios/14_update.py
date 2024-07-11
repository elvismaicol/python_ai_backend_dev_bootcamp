# Atualiza o dicionario 
# Ao passar uma chave que já existe, o valor dessa chave será atualizado para os novo vlr

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  
# {'guilherme@gmail.com': {'nome': 'Gui'}}

# Se a chave não existir, a chave será incluida como uma nova cheve no dicionario
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)