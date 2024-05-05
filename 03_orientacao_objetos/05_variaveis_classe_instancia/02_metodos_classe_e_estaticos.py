class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # tranforma em um metodo de classe | usa-se por convenção "cls" ao invés de "self"
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    # Mestodo estático
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa("ELvis", 43)
#print(p)

#p = Pessoa().criar_de_data_nascimento(1980, 3, 1, "Elvis")
#print(p.nome, p.idade)

# fazendo uso do @classmethod:
p = Pessoa.criar_de_data_nascimento(1980, 3, 1, "Elvis")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))