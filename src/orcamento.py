from src.alerta import Alerta
from database.database import lerJsonSettings, lerJsonLancamentos

class Orcamento:
    def __init__(self):                
        self.alerta_sistema = Alerta()

    def saldoGlobal(self):
        lancamentosCriados = lerJsonLancamentos()
        receita = 0
        despesa = 0
        for i in lancamentosCriados:
            if i['tipo'] == 'receita':
                receita += i['valor']
            elif i['tipo'] == 'despesa':
                despesa += i['valor']
        saldo = receita - despesa
        return saldo, receita, despesa

    def calcular_saldo_mensal(self, mes, ano):
        lancamentosCriados = lerJsonLancamentos()  
        total_receitas = 0.0
        total_despesas = 0.0
        for i in lancamentosCriados:                    
            # Filtra pelo mês e ano
            if i['data'][1] == int(mes) and i['data'][2] == int(ano):                
                if i['tipo'] == "receita":                    
                    total_receitas += i['valor']
                elif i['tipo'] == "despesa":                    
                    total_despesas += i['valor']
        return total_receitas - total_despesas

    def calcular_saldo_diario(self, dia, mes, ano):
        lancamentosCriados = lerJsonLancamentos()  
        saldo_dia = 0.0
        for i in lancamentosCriados:
            if i['data'][0] == int(dia) and i['data'][1] == int(mes) and i['data'][2] == int(ano):
                if i['tipo'] == "receita":
                    saldo_dia += i['valor']
                elif i['tipo'] == "despesa":
                    saldo_dia -= i['valor']            
        return saldo_dia
