from financeiro import Financeiro

financeiro = Financeiro()

while True:

    print("\n===== CONTROLE FINANCEIRO =====")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar Transações")
    print("4 - Mostrar Saldo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        categoria = input("Categoria: ")

        financeiro.adicionar_transacao(
            descricao,
            valor,
            categoria,
            "Receita"
        )

        print("Receita cadastrada com sucesso!")

    elif opcao == "2":

        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        categoria = input("Categoria: ")

        financeiro.adicionar_transacao(
            descricao,
            valor,
            categoria,
            "Despesa"
        )

        print("Despesa cadastrada com sucesso!")

    elif opcao == "3":

        transacoes = financeiro.listar_transacoes()

        if not transacoes:
            print("Nenhuma transação cadastrada.")
        else:
            for transacao in transacoes:
                print("-" * 30)
                print(f"Data: {transacao.data}")
                print(f"Tipo: {transacao.tipo}")
                print(f"Descrição: {transacao.descricao}")
                print(f"Categoria: {transacao.categoria}")
                print(f"Valor: R$ {transacao.valor:.2f}")

    elif opcao == "4":

        saldo = financeiro.calcular_saldo()

        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "5":

        print("Até logo!")
        break

    else:
        print("Opção inválida.")