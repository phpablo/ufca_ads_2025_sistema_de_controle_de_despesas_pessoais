from src.alerta import Alerta
from database.database import lerJsonSettings

class Orcamento:
    def __init__(self, orcamento_total: float):
        self.orcamento_total = orcamento_total
        self.lista_lancamentos = []
        self.alerta_sistema = Alerta()

    # def adicionar_lancamento(self, lancamento):
    #     self.lista_lancamentos.append(lancamento)
    #     self.verificar_alertas(lancamento)

    def calcular_saldo_mensal(self, mes, ano):
        total_receitas = 0.0
        total_despesas = 0.0

        for item in self.lista_lancamentos:
            # Filtra pelo mês e ano
            if item.data.month == mes and item.data.year == ano:
                if item.categoria == "RECEITA":
                    total_receitas += item.valor
                elif item.categoria == "DESPESA":
                    total_despesas += item.valor

        return total_receitas - total_despesas

    def calcular_saldo_diario(self, dia, mes, ano):
        saldo_dia = 0.0
        for item in self.lista_lancamentos:
            if item.data.day == dia and item.data.month == mes and item.data.year == ano:
                if item.categoria == "RECEITA":
                    saldo_dia += item.valor
                elif item.categoria == "DESPESA":
                    saldo_dia -= item.valor
        return saldo_dia

    def verificar_alertas(self, item_recente):
        # Regra 1: Déficit
        config_alto_valor = lerJsonSettings()
        saldo_mes = self.calcular_saldo_mensal(item_recente.data.month, item_recente.data.year)
        if saldo_mes < 0:
            self.alerta_sistema.emitir_alerta_deficit(saldo_mes)

        # Regra 2: Alto Valor (Despesa > 500)
        if item_recente.categoria == "DESPESA" and item_recente.valor > config_alto_valor["alto_valor_de_despesa"]:
            self.alerta_sistema.emitir_alerta_alto_valor(item_recente.valor, item_recente.descricao)