# Trabalhando com váriavés com escopo local e global

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(500))
# 2500