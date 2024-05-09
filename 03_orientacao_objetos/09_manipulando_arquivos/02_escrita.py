file_lorem = "/python_ai_backend_dev_bootcamp/03_orientacao_objetos/09_manipulando_arquivos/teste.txt"

arquivo = open(file_lorem, "w")

arquivo.write("Escrevendo dados em um arquivo.")
arquivo.writelines(["\n", "Escrevendo ", "\n", "um ", "\n", "novo ", "\n", "texto."])
arquivo.close()

#print(arquivo.read())

# retorna 1 linha
#print(arquivo.readline())
#print(arquivo.readline())

# retorna o conteudo dentro de uma lista
#print(arquivo.readlines())

#while len(linha := arquivo.readline()):
#    print(linha)
    
