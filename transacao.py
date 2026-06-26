from datetime import datetime

class Transacao:
    
    def __init__(self, descricao, valor, categoria, tipo):
        
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.data = datetime.now().strftime("%d/%m/%Y")
        
    def to_dict(self):
        return {
            'descricao': self.descricao,
            'valor': self.valor,
            'categoria': self.categoria,
            'tipo': self.tipo,
            'data': self.data
        }
        