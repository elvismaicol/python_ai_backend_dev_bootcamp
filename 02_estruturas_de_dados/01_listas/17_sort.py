# Ordena a lista
# Aceita parametros

# Default: ordena em ordem alfabética
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Ordena invertendo a ordem da lista
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# Usando função anônima(lambda), como argumento, para organizar a lista por tamanho do objeto
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  
print(linguagens)
# ["c", "js", "java", "python", "csharp"]


# Usando função anônima(lambda), como argumento, para organizar a lista por tamanho do objeto
# Com o reverse para colocar em ordem invertida(decrescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  
print(linguagens)

# ["python", "csharp", "java", "js", "c"]