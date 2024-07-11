# Definindo menu
menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=>
"""

# Definindo variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe do valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe do valor do saque: "))

        excedeu_saldo = valor > saldo
  
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("A operação falhou! O número máximo de saques foi excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("A operação falhou! O valor informado é inválido.")            

    elif opcao == "e":
        extrato_str = " EXTRATO "
        print(extrato_str.center(60, "="))
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(60 * "=")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
