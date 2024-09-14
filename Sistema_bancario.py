menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def deposito(saldo, extrato):

    deposito = float(input("Informe o valor do deposito: "))

    if deposito <= 0:
        print("O valor informado e invalido")
        return saldo, extrato

    saldo += deposito
    extrato += f"Deposito: R$ {deposito:5.2f}\n"
    print(f"Deposito de R$ {deposito:5.2f}")
    return saldo, extrato


def saque(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):

    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saque diario atingido!")
        return saldo, numero_saques, extrato

    saque = float(input("Informe o valor do saque: "))

    if saque > limite:
        print(f"O valor limite = R$ {limite:5.2f}")
        return saldo, numero_saques, extrato

    if saque > saldo:
        print("Saldo insuficiente!")
        return saldo, numero_saques, extrato

    if saque <= 0:
        print("O valor informado e invalido")
        return saldo, numero_saques, extrato

    print(f"Saque de R$ {saque:5.2f} realizado com sucesso!")
    saldo -= saque
    extrato += f"Saque:    R$ {saque:5.2f}\n"
    numero_saques += 1
    return saldo, numero_saques, extrato


def exibir_extrato(extrato, saldo):
    print(f"\nExtrato bancario\n{extrato}")
    print()
    print(f"Saldo: R$ {saldo:.2f}")


while True:

    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = deposito(saldo, extrato)
    elif opcao == "2":
        saldo, numero_saques, extrato = saque(
            saldo, limite, extrato, numero_saques, LIMITE_SAQUES
        )
    elif opcao == "3":
        exibir_extrato(extrato, saldo)
    elif opcao == "0":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")
