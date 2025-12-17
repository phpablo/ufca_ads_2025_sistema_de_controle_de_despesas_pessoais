class Alerta:
    def __init__(self):
        self.logs = []

    def emitir_alerta_alto_valor(self, despesa_valor, despesa_descricao):
        mensagem = f"⚠️ ALERTA: Despesa de Alto Valor! R$ {despesa_valor:.2f} - {despesa_descricao}"
        print(mensagem)
        self.logs.append(mensagem)

    def emitir_alerta_limite_categoria(self, categoria, excesso):
        mensagem = f"⚠️ ALERTA: Limite de '{categoria}' excedido em R$ {excesso:.2f}!"
        print(mensagem)
        self.logs.append(mensagem)

    def emitir_alerta_deficit(self, saldo_atual):
        mensagem = f"🚨 ALERTA CRÍTICO: Déficit Orçamentário! Saldo negativo: R$ {saldo_atual:.2f}"
        print(mensagem)
        self.logs.append(mensagem)