from src.lancamento import Lancamento
from database.database import salvarJsonLancamentos, lerJsonLancamentos
from database.database import lerJsonCategorias
from src.alerta import Alerta

class Despesa(Lancamento):
    def __init__(self, valor: float, categoria, descricao: str, formas_pagamento: str, tipo: str):
        super().__init__(valor, categoria, descricao, formas_pagamento, tipo)
        self.tipo = tipo
        
    def __str__(self):
        return f'Despesa | Data: {self.data} | Categoria: {self.categoria} | Valor: {self.valor} | Forma de pagamento: {self.formas_pagamento}'

    @staticmethod
    def verificarAltoValor(valor, categoria):
        alerta = Alerta()
        for cat in lerJsonCategorias():
            if valor > cat['limite_mensal'] and categoria == cat['nome']:
                alerta.emitir_alerta_alto_valor(valor, categoria)
        return None

    def salvarDespesa(self):
        receitasJson = lerJsonLancamentos()        
        receita = {
            "valor": self.valor,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "forma_pagamento": self.formas_pagamento,
            "data": self._data,
            "tipo": self.tipo
        }
        self.verificarAltoValor(self.valor, self.categoria)
        receitasJson.append(receita)
        salvarJsonLancamentos(receitasJson)

   