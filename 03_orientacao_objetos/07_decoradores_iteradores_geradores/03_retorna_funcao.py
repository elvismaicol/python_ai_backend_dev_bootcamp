def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    operacoes = {
        "+": soma,
        "-": sub,
        "*": mul,
        "/": div
    }

    return operacoes.get(operacao, lambda a, b: None)  # Retorna uma função lambda como padrão

# usar no python ver~so superior a 3.10
'''
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
'''

op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))