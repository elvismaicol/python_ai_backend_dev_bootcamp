# Formas de declarar dicionario

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)
 # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)
 # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

pessoa["telefone"] = "3333-1234" 
print(pessoa)
 # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}