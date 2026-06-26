from flask import Flask, render_template_string
from financeiro import Financeiro

app = Flask(__name__)
financeiro = Financeiro()


@app.route("/")
def dashboard():

    transacoes = financeiro.listar_transacoes()

    receitas = 0
    despesas = 0
    categorias = {}

    for t in transacoes:

        if t.tipo.lower() == "receita":
            receitas += t.valor
        else:
            despesas += t.valor

        categorias[t.categoria] = categorias.get(t.categoria, 0) + t.valor

    saldo = receitas - despesas

    html = f"""
    <html>
    <head>
        <title>Dashboard Financeiro</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}
            .card {{
                padding: 15px;
                margin: 10px;
                border: 1px solid #ccc;
                border-radius: 10px;
                width: 250px;
            }}
        </style>
    </head>
    <body>

        <h1>💰 Dashboard Financeiro</h1>

        <div class="card">
            <h3>Receitas</h3>
            <p>R$ {receitas:.2f}</p>
        </div>

        <div class="card">
            <h3>Despesas</h3>
            <p>R$ {despesas:.2f}</p>
        </div>

        <div class="card">
            <h3>Saldo</h3>
            <p>R$ {saldo:.2f}</p>
        </div>

        <h2>Categorias</h2>
        <ul>
            {"".join([f"<li>{k}: R$ {v:.2f}</li>" for k, v in categorias.items()])}
        </ul>

    </body>
    </html>
    """

    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)