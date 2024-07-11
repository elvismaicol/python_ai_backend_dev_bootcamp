# Exemplo com objetos de 1ª Classe

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(32, 10, somar)  
# O resultado da operação 10 + 10 = 20