# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
qtd_itens = 1
while qtd_itens <= 3:
# TODO: Solicite o item e armazena na variável "item":
  item = input("Informe o item para armazenamento: ")
# TODO: Adicione o item à lista "itens":
  itens.append(item)
  print(f"O {qtd_itens}º item foi armazenado!")
  qtd_itens += 1

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")