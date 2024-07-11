class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Elvis", "0001")

aluno_2 = Estudante("Suélen", "0002")

mostrar_valores(aluno_1, aluno_2)

# Altera para toda classe
Estudante.escola = "Python"
# vai alterar para apenas o aluno_1
#aluno_1.escola = "Python"

aluno_3 = Estudante("Melissa", "0003")

mostrar_valores(aluno_1, aluno_2, aluno_3)
