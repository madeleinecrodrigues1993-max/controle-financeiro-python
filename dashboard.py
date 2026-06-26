import matplotlib.pyplot as plt
from financeiro import Financeiro


def gerar_dashboard():

    financeiro = Financeiro()
    transacoes = financeiro.listar_transacoes()

    receitas = 0
    despesas = 0
    categorias = {}

    for t in transacoes:

        if t.tipo.lower() == "receita":
            receitas += t.valor
        else:
            despesas += t.valor

        if t.categoria in categorias:
            categorias[t.categoria] += t.valor
        else:
            categorias[t.categoria] = t.valor

    plt.figure("Dashboard Financeiro")

    # Gráfico 1
    plt.subplot(1, 2, 1)
    plt.bar(["Receitas", "Despesas"], [receitas, despesas])
    plt.title("Receitas vs Despesas")

    # Gráfico 2
    plt.subplot(1, 2, 2)
    plt.pie(
        categorias.values(),
        labels=categorias.keys(),
        autopct="%1.1f%%"
    )
    plt.title("Gastos por Categoria")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    gerar_dashboard()