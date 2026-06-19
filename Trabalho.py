print("--- BANCO DINHEIRO SEGURO ---")

saldo = 500.00
cheque_especial = 200.00

while True:

    # Encerra ao atingir o limite do cheque especial
    if saldo <= -200:
        print("Limite do cheque especial atingido.")
        print("Sessão encerrada.")
        break

    print(f"\nSeu saldo atual: R$ {saldo:.2f}")
    print("[1] Sacar | [2] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_saque = float(input("Digite o valor do saque: R$ "))

        # Não permite valores negativos ou zero
        if valor_saque <= 0:
            print("Erro: Digite um valor maior que zero.")

        # Verifica se o saque ultrapassa o total disponível
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