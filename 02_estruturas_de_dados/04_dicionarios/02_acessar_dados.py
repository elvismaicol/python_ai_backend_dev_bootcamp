# Formas de acessar dados em dicionários e alterar dados das chaves

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(dados)  
# {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'}

print(dados["nome"])  
# "Guilherme"

print(dados["idade"])  
# 28

print(dados["telefone"])  
# "3333-1234"

# alterando dados do dicionário
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  
# {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}