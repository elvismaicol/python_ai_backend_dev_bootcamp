# Verifica se uma chave existe no dicionario 

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# verifica se "guilherme@gmail.com" é uma chave no dicionario contatos
resultado = "guilherme@gmail.com" in contatos  
print(resultado)
# True

resultado = "megui@gmail.com" in contatos  
print(resultado)
# False

# verificando se existe uma chave no dicionario mais interno
resultado = "idade" in contatos["guilherme@gmail.com"]  
print(resultado)
# False

print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"] 
print(resultado)
 # True