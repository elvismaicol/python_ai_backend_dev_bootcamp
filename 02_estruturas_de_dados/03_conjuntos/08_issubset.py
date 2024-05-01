# Verifica se um conjunto é subconjunto de outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Verificando se os elementos de conjunto_a estão contidos no conjunto_b
# conjunto_a Pertence conjunto_b
resultado = conjunto_a.issubset(conjunto_b)  
print(resultado)
# True

# Verificando se os elementos de conjunto_b estão contidos no conjunto_a
# conjunto_b Pertence conjunto_a
resultado = conjunto_b.issubset(conjunto_a)  
print(resultado)
# False