import datetime

menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

    -> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

data = datetime.datetime.now()
data_str = data.strftime("%A %d %B %y %I:%M")
data_atual = datetime.datetime.strptime(data_str,"%A %d %B %y %I:%M")

extrato = []


while True:
    opcao = input(menu)
    if opcao == '1':
        valor_deposito = float(input("Depositar: "))

        valor_negativo = valor_deposito < 0
        
        if valor_negativo:
            print("Seu saque deve ser positivo.")

        elif valor_deposito > 0:
            saldo += valor_deposito
            print(f"Valor de R${valor_deposito} depositado!")
            extrato.append((data_atual, f"Depósito", f"+R${valor_deposito}", saldo))

        else:
            print("O depósito tem que ser maior de 0 reais. Deposite um valor maior.")

    elif opcao == '2':
        valor_saque = float(input("Sacar: "))
        numero_saques += 1


        if valor_saque < 0:
            print("Seu saque deve ser positivo.")
        elif saldo < valor_saque:
            print("Saldo insuficiente.")
        elif valor_saque > limite:
            print("O valor do saque excede o limite.")
        elif numero_saques > LIMITE_SAQUES:
            print("Você já atingiu seu limite de saques por dia.")
        else:
            saldo -= valor_saque
            data_atual = datetime.datetime.now()
            extrato.append((data_atual, f"Saque   ", f"-R${valor_saque}", saldo))
            print("Sacando...")
            print(f"Valor de R${valor_saque} sacado!")
                

    elif opcao == '3':
        print("\nExtrato:")

        if len(extrato) == 0:
            print("Nenhuma movimentação feita.")
        else:
            print("Data             | Tipo     | Valor    | Saldo")
            for movimento in extrato:
                data_mov, tipo, valor, saldo_apos_mov = movimento
                print(f"{data_mov.strftime('%d/%m/%Y %H:%M')} | {tipo:<5} | {valor:>5} | {saldo_apos_mov}")

    elif opcao == '4':
        print(f"\nSaldo final: {saldo}")
        print("\nSaindo...")
        break

    else:
        print("ERROR! Opção inválida")
        continue

    

