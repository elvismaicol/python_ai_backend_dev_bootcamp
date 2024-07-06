file_lorem = "/python_ai_backend_dev_bootcamp/03_orientacao_objetos/09_manipulando_arquivos/lorem.txt"

arquivo = open(file_lorem, "r")

#print(arquivo.read())

# retorna 1 linha
#print(arquivo.readline())
#print(arquivo.readline())

# retorna o conteudo dentro de uma lista
#print(arquivo.readlines())

while len(linha := arquivo.readline()):
    print(linha)
    
arquivo.close()