# Acessando o valor de uma chave usando GET

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# No modo abaixo se a chave não existitir ocorrerá um erro
# contatos["chave"]  # KeyError

#Usando get() se a chave não existitir vai retornar None
resultado = contatos.get("chave")  
print(resultado)
# None

# pod ser passado um argumento default para se não encontrar a chave trazer esse argumento ex:{}
resultado = contatos.get("chave", {}) 
print(resultado)
# {}

resultado = contatos.get(
    "guilherme@gmail.com", {}
) 
print(resultado)
# {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}