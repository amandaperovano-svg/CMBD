print("--- BANCO DINHEIRO SEGURO ---")

saldo = 500.00
cheque_especial = 200.00

while True:
    print(f"\nSeu saldo atual: R$ {saldo:.2f}")
    print("[1] Sacar | [2] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_saque = float(input("Digite o valor do saque: R$ "))

        # Verifica se o valor é válido
        if valor_saque <= 0:
            print("Erro: Digite um valor maior que zero.")

        # Verifica se ultrapassa o saldo + cheque especial
        elif valor_saque > (saldo + cheque_especial):
            print("Erro: Saldo e limite insuficientes para este saque.")

        else:
            saldo = saldo - valor_saque
            print("Saque realizado com sucesso!")

            if saldo < 0:
                print("Atenção: Você entrou no uso do Cheque Especial!")

    elif opcao == "2":
        print("Sessão encerrada.")
        break

    else:
        print("Erro: Opção inválida! Escolha 1 ou 2.")