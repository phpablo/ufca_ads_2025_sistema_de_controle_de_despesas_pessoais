from datetime import date
from src.categoria import Categoria
from database.database import lerJsonCategorias

class Lancamento:   
    def __init__(self, valor: float, categoria:str, descricao: str, formas_pagamento: str, tipo:str):       
        categoriasCriadas = lerJsonCategorias()           
        try:
            valor = float(valor)
        except:
            raise ValueError('O valor deve ser um número')
        if valor <= 0:
            raise ValueError("O valor deve ser maior do que zero.")
        else:
            self.__valor = valor
        
        for i in categoriasCriadas:
            if i['nome'] == categoria and i['tipo'] == tipo:
                self.categoria = i['nome'] 
                break                         
        else:
            raise ValueError ('Categoria não encontrada')
        
        self._data = (date.today().day, date.today().month, date.today().year)

        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError('Descrição inválida')
        else:
            self.__descricao = descricao
        opcoes_validas = ["DINHEIRO", "DEBITO", "CREDITO", "PIX"]
        if formas_pagamento.upper() not in opcoes_validas:
            raise ValueError("Forma de pagamento inválida!")
        else:
            self.__formas_pagamento = formas_pagamento.upper()

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Valor inválido.")
        self.__valor = float(valor)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_lancamento):
        if not isinstance(data_lancamento, date):
            raise TypeError("Data inválida.")
        self._data = data_lancamento

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, new_descricao):
        if (not isinstance(new_descricao, str)) or (not new_descricao.strip()):
            raise ValueError('Descrição inválida')
        self.__descricao = new_descricao

    @property
    def formas_pagamento(self):
        return self.__formas_pagamento

    @formas_pagamento.setter
    def formas_pagamento(self, formas_pagamento):
        opcoes_validas = ["DINHEIRO", "DEBITO", "CREDITO", "PIX"]
        if formas_pagamento not in opcoes_validas:
            raise ValueError("Forma de pagamento inválida!")
        self.__formas_pagamento = formas_pagamento.upper()

# Métodos especiais

    # Resumo de lançamento
    def __str__(self):
        return(
            f"{self.data} | {self.categoria.nome} | "
            f"R$ {self.valor:.2f} | {self.__formas_pagamento}"
        )

    #Detalhamento interno
    def __repr__(self):
        return (
            f"Lancamento(valor={self.valor}, "
            f"categoria={self.categoria.nome}, "
            f"data={self.data}, "
            f"forma_pagamento='{self.__formas_pagamento}')"
        )

    #Comparação por ID ou data + descrição
    def __eq__(self, other):
        if not isinstance(other, Lancamento):
            return False
        return (
                self.data == other.data and
                self.descricao == other.descricao and
                self.valor == other.valor
        )

    #Ordenação por data ou valor
    def __lt__(self, other):
        return self.data < other.data