from transacao import Transacao


class Financeiro:

    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao, valor, categoria, tipo):

        transacao = Transacao(
            descricao,
            valor,
            categoria,
            tipo
        )

        self.transacoes.append(transacao)

    def listar_transacoes(self):
        return self.transacoes

    def calcular_saldo(self):

        saldo = 0

        for transacao in self.transacoes:

            if transacao.tipo.lower() == "receita":
                saldo += transacao.valor
            else:
                saldo -= transacao.valor

        return saldo