# O contrario do issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Verificando se todos os elementos de conjunto_b estão contidos no conjunto_a
resultado = conjunto_a.issuperset(conjunto_b)  
print(resultado)
# False

# Verificando se todos os elementos de conjunto_a estão contidos no conjunto_b
resultado = conjunto_b.issuperset(conjunto_a)  
print(resultado)
# True