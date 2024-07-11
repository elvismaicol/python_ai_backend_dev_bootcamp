# Retona a diferença

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Retornará os itens que existem no conjunto_a que não existem no conjunto_b
resultado = conjunto_a.difference(conjunto_b)
print(resultado)
# {1}

# Retornará os itens que existem no conjunto_b que não existem no conjunto_a
resultado = conjunto_b.difference(conjunto_a)
print(resultado)
# {4}