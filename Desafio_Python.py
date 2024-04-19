menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[O] Sair

--->
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    if opcao == "d":
        print( "Depósito" )
        valor = float( input("Digite o valor a ser depositado e logo após \nconfirmaremos o depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: ("A operação falhou, informe um número válido.")


    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Atividade inválida, você não possui saldo.")

        elif excedeu_limite:
            print("Atividade inválida, você não possui limite")

        elif excedeu_saques:
            print("Você excedeu o limite de saques diários, volte novamente amanhã.")
        elif valor> 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: print("Operação inválida")


    elif opcao == "e":
        print("\n--------Extrato--------")
        print(f"Você possui R${saldo:.2f} na sua conta.")
        print("---------------")


    elif opcao == "o":
        break
    else:
        print("Operação inválida, selecione uma operação")





