# Usado para criar chaves para adicionar no dicionario

resultado = dict.fromkeys(["nome", "telefone"])  
print(resultado)
# {"nome": None, "telefone": None}

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  
print(resultado)
# {"nome": "vazio", "telefone": "vazio"}
