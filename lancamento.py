from datetime import date
#from models.categoria import Categoria

class Lancamento:
    def __init__(self, valor: float, categoria, data, descricao: str, formas_pagamento: str):
        self.__valor = valor
        self.__categoria = categoria #Chamar a classe categoria
        self.__data = data if data else date.today()
        self.__descricao = descricao
        self.__formas_pagamento = formas_pagamento

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Valor inválido.")
        self.__valor = float(valor)

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        #if not isinstance(categoria, Categoria):
        #    raise TypeError("Categoria Inválida")
        self.__categoria = categoria

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
        opcoes_validas = ["Dinheiro", "Débito", "Crédito", "PIX"]
        if formas_pagamento not in opcoes_validas:
            raise ValueError("Forma de pagamento inválida!")
        self.__formas_pagamento = formas_pagamento.lower()

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