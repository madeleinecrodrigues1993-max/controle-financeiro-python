import json
import os

from transacao import Transacao


class Financeiro:

    def __init__(self):
        self.transacoes = []
        self.arquivo = "dados/movimentacoes.json"

        self.carregar_dados()

    def carregar_dados(self):

        if not os.path.exists(self.arquivo):
            return

        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:

                dados = json.load(arquivo)

                for item in dados:

                    transacao = Transacao(
                        item["descricao"],
                        item["valor"],
                        item["categoria"],
                        item["tipo"]
                    )

                    transacao.data = item["data"]

                    self.transacoes.append(transacao)

        except (json.JSONDecodeError, FileNotFoundError):
            self.transacoes = []

    def salvar_dados(self):

        dados = []

        for transacao in self.transacoes:
            dados.append(transacao.to_dict())

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    def adicionar_transacao(self, descricao, valor, categoria, tipo):

        transacao = Transacao(
            descricao,
            valor,
            categoria,
            tipo
        )

        self.transacoes.append(transacao)
        self.salvar_dados()

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