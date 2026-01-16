from src.lancamento import Lancamento
from database.database import salvarJsonLancamentos, lerJsonLancamentos

class Receita(Lancamento):
    def __init__(self, valor: float, categoria, descricao: str, formas_pagamento: str, tipo: str):
        super().__init__(valor, categoria, descricao, formas_pagamento, tipo)
        self.__tipo = tipo

    def __str__(self):
        return f'Receita | Data: {self.data} | Categoria: {self.categoria.nome} | Valor: {self.valor} | Forma de pagamento: {self.formas_pagamento}'
    
    def salvarReceita(self):
        receitasJson = lerJsonLancamentos()
        
        receita = {
            "valor": self.valor,
            "categoria": self.categoria['nome'],
            "descricao": self.descricao,
            "forma_pagamento": self.formas_pagamento,
            "data": self._data,
            "tipo": self.__tipo
        }
        receitasJson.append(receita)
        salvarJsonLancamentos(receitasJson)