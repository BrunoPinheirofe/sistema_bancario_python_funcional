from datetime import datetime

menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""


def depositar(valor_deposito: float):
    global saldo, extrato
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"deposito de {valor_deposito:.2f}----{datetime.now().strftime('%d/%m/%Y'):>60}\n"
        print(f"{valor_deposito} adicionado ao saldo")

    else:
        print("valor informado para deposito é invalido")


def sacar(valor_saque: float):
    global saldo, limite, extrato, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("Valor maximo de saques por dia atingido!")
    else:
        if valor_saque > 0:
            if valor_saque > limite:
                print(
                    f"Valor informado é maior que o limite permitido de {limite:.2f}R$ "
                )
            else:
                saldo -= valor_saque
                extrato += f"saque de {valor_saque} ---- {datetime.now().strftime('%d/%m/%Y'):>60}\n"
                numero_saques += 1
                print(f"{valor_saque} descontado da conta")
        else:
            print("Valor informado para saque é invalido")


def mostra_extrato():
    print("EXTRATO".center(50, "-"))
    print(extrato)
    print(f"saldo{saldo:>30}")


while True:

    opcao = input(menu).lower()
    print(opcao)
    if opcao == "d":
        depositar(float(input("digite qual é o valor do deposito R$:")))
    elif opcao == "s":
        sacar(float(input("digite qual é o valor do sacar R$:")))
    elif opcao == "e":
        mostra_extrato()
    elif opcao == "q":
        print("Saindo do programa...")
        break
