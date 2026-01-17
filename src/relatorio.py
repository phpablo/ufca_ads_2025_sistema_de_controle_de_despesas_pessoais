from database.database import lerJsonLancamentos

def comparativo_receitas_despesas():
    lancamentos = lerJsonLancamentos()
    total_por_mes = {}

    for lancamento in lancamentos:
        data = lancamento.get('data')
        if not data:
            continue

        mes = data[1]
        ano = data[2]
        chave = (ano, mes)

        if chave not in total_por_mes:
            total_por_mes[chave] = {'receita': 0, 'despesa': 0}

        tipo = lancamento.get('tipo')
        valor = lancamento.get('valor', 0)

        if tipo == 'receita':
            total_por_mes[chave]['receita'] += valor
        elif tipo == 'despesa':
            total_por_mes[chave]['despesa'] += valor

    meses_ordenados = sorted(total_por_mes.keys(), reverse=True)

    print("\n=== COMPARATIVO DE RECEITAS E DESPESAS (últimos 3 meses) ===")
    print(f"{'Mês/Ano':<10} {'Receitas':>10} {'Despesas':>10} {'Saldo':>10}")

    for chave in meses_ordenados[:3]:
        ano, mes = chave
        receita = total_por_mes[chave]['receita']
        despesa = total_por_mes[chave]['despesa']
        saldo = receita - despesa
        print(f"{mes:02d}/{ano}  R$ {receita:>8.2f}  R$ {despesa:>8.2f}  R$ {saldo:>8.2f}")

    input("\nPressione ENTER para voltar...")

def mes_mais_economico():
    lancamentos = lerJsonLancamentos()
    total_por_mes = {}

    for lancamento in lancamentos:
        if lancamento.get('tipo') == 'despesa':
            data = lancamento.get('data')
            valor = lancamento.get('valor', 0)

            if not data:
                continue

            # data = [dia, mes, ano]
            mes = data[1]
            ano = data[2]

            chave = (mes, ano)

            if chave not in total_por_mes:
                total_por_mes[chave] = 0

            total_por_mes[chave] += valor

    # encontra o mês com menor gasto
    mes_economico = min(total_por_mes, key=total_por_mes.get)
    menor_total = total_por_mes[mes_economico]

    mes, ano = mes_economico

    print("\n=== MÊS MAIS ECONÔMICO ===")
    print(f"{mes:02d}/{ano} → R$ {menor_total:.2f}")

    input("\nPressione ENTER para voltar...")
def percentual_despesas_por_categoria():
   lancamentos = lerJsonLancamentos()
   total_por_categoria = {}
   total_geral = 0

   for lancamento in lancamentos:
       if lancamento.get('tipo') == 'despesa':
           categoria = lancamento.get('categoria')
           valor = lancamento.get('valor',0)

           if categoria not in total_por_categoria:
               total_por_categoria[categoria] = 0
           total_por_categoria[categoria] += valor
           total_geral += valor

   print("\n=== PERCENTUAL DE DESPESAS POR CATEGORIA ===")

   for categoria, total in total_por_categoria.items():
       percentual = (total / total_geral) * 100
       print(f"{categoria:<25} R$ {total:>8.2f} {percentual:>6.2f}%")
   print("-" * 30)
   print(f"{'TOTAL':<25}  R$ {total_geral:>8.2f}  100.00%")
   input("\nPressione ENTER para voltar...")

def despesas_por_forma_pagamento():
    lancamentos = lerJsonLancamentos()
    total_por_forma = {}

    for lancamento in lancamentos:
        if lancamento.get('tipo') == 'despesa':
            forma = lancamento.get('forma_pagamento')
            valor = lancamento.get('valor',0)
            if forma not in total_por_forma:
                total_por_forma[forma] = 0
            total_por_forma[forma] += valor

    print("\n=== DESPESAS POR FORMA DE PAGAMENTO ===")
    for forma, total in total_por_forma.items():
        print(f"{forma:<25}  R$ {total:>8.2f}")
    input("\nPressione ENTER para voltar...")

def total_despesas_por_categoria():
    lancamentos = lerJsonLancamentos()
    total_por_categoria = {}

    for lancamento in lancamentos:
        if lancamento['tipo'] == 'despesa':
            categoria = lancamento['categoria']
            valor = lancamento['valor']

            if categoria not in total_por_categoria:
                total_por_categoria[categoria] = 0

            total_por_categoria[categoria] += valor

    print("\n=== TOTAL DE DESPESAS POR CATEGORIA ===")
    for categoria, total in total_por_categoria.items():
       # print(f"{categoria}: R$ {total:.2f}")
       print(f"{categoria:<25} R$ {total:>8.2f}")

    input("\nPressione ENTER para voltar...")

if __name__ == "__main__":
    percentual_despesas_por_categoria()
