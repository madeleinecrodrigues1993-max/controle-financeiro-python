# Controle Financeiro Pessoal

Sistema de controle financeiro desenvolvido em Python com persistência de dados, relatórios automáticos e dashboard interativo com visualização de gráficos.

---

## Sobre o projeto

Este projeto tem como objetivo simular um sistema financeiro pessoal, permitindo o gerenciamento de receitas e despesas, cálculo de saldo, geração de relatórios e visualização de dados em forma de gráficos.

Ele foi desenvolvido como forma de estudo de:

* Programação Orientada a Objetos (POO)
* Manipulação de arquivos (JSON e TXT)
* Desenvolvimento web com Flask
* Visualização de dados com Chart.js e Matplotlib

---

## Funcionalidades

* Cadastro de receitas e despesas
* Listagem de transações
* Cálculo automático de saldo
* Persistência de dados em JSON
* Geração de relatório financeiro (.txt)
* Dashboard em terminal
* Dashboard gráfico com Matplotlib
* Dashboard web com Flask
* Gráficos interativos com Chart.js

---

## Tecnologias utilizadas

* Python 3
* Flask
* JSON
* Matplotlib
* Chart.js
* HTML e CSS básico

---

## Estrutura do projeto

```text
controle-financeiro/
│
├── main.py              # Menu principal (terminal)
├── app.py               # Dashboard web (Flask)
├── dashboard.py         # Dashboard com gráficos (matplotlib)
├── financeiro.py        # Lógica financeira principal
├── transacao.py         # Classe de transações
├── utils.py             # Funções auxiliares
│
├── dados/
│   └── movimentacoes.json
│
├── relatorios/
│   └── relatorio.txt
│
└── README.md
```

---

## Como executar o projeto

### Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/controle-financeiro-python.git
```

### Instalar dependências

```bash
pip install flask matplotlib
```

### Executar versão em terminal

```bash
python main.py
```

### Executar dashboard web

```bash
python app.py
```

Acessar no navegador:

```
http://127.0.0.1:5000
```

### Executar dashboard gráfico

```bash
python dashboard.py
```

---

## Demonstração

Adicione aqui imagens do sistema em execução, como:

* Menu no terminal
* Dashboard web
* Gráficos de receitas e despesas
* Gráfico por categorias

---

## Aprendizados

Este projeto reforçou conhecimentos em:

* Estruturação de projetos em Python
* Programação orientada a objetos
* Manipulação de arquivos
* Separação de responsabilidades
* Visualização de dados
* Integração entre backend e frontend

---

## Possíveis melhorias

* Autenticação de usuários
* Banco de dados SQLite
* Filtros por mês e ano
* Exportação em PDF
* Deploy em ambiente online

---

## Autor

Madeleine Rosa

Projeto desenvolvido para portfólio de desenvolvimento em Python.

---
