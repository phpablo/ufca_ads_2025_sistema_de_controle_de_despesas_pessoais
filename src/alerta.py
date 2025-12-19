class Alerta:
    def __init__(self):
        self.logs = []

    def emitir_alerta_alto_valor(self, despesa_valor, despesa_descricao):
        mensagem = f"⚠️ \033[31mALERTA: Despesa de Alto Valor! \033[1mR$ {despesa_valor:.2f} - {despesa_descricao}\033[m"
        print(mensagem)
        self.logs.append(mensagem)

    def emitir_alerta_limite_categoria(self, categoria, excesso):
        mensagem = f"⚠️ \033[31mALERTA: Limite de '{categoria}' excedido em R$ {excesso:.2f}!\033[m"
        print(mensagem)
        self.logs.append(mensagem)

    def emitir_alerta_deficit(self, saldo_atual):
        mensagem = f"🚨 \033[31mALERTA CRÍTICO: Déficit Orçamentário! \033[1mSaldo negativo: R$ {saldo_atual:.2f}\033[m"
        print(mensagem)
        self.logs.append(mensagem)