# Exclui um chave do dicionario
# pode recer um valor default para retornar caso não encontre a chave
# ao remover, o pop() retorna o item removido

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  
print(resultado)
# {'nome': 'Guilherme', 'telefone': '3333-2221'}

resultado = contatos.pop("guilherme@gmail.com", {}) 
print(resultado)
# {}