from src.lancamento import Lancamento

class Receita(Lancamento):
    def __init__(self, valor: float, categoria, data, descricao: str, formas_pagamento: str):
        super().__init__(valor, categoria, data, descricao, formas_pagamento)

    def emitir_relatorio(self):
        return f'Receita | Data: {self.data} | Categoria: {self.categoria.nome} | Valor: {self.valor} | Forma de pagamento: {self.formas_pagamento}'