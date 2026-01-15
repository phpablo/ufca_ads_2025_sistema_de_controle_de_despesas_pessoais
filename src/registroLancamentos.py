from database.database import lerJsonLancamentos, salvarJsonLancamentos
from src.receita import Receita
from src.despesa import Despesa

def criarReceita():
  print('\nRegistrar receita no sistema')
  valor = float(input('Valor da receita: '))
  categoria = input('Nome da receita: ')
  descricao = input('Descrição: ')
  forma_pagamento = input('Forma de pagamento (DINHEIRO, PIX, DEBITO, CREDITO): ')

  nova_receita = Receita(valor, categoria, descricao, forma_pagamento, 'receita')
  nova_receita.salvarReceita()

def criarDespesa():
  print('\nRegistrar despesa no sistema')
  valor = float(input('Valor da despesa: '))
  categoria = input('Nome da despesa: ')
  descricao = input('Descrição: ')
  forma_pagamento = input('Forma de pagamento (DINHEIRO, PIX, DEBITO, CREDITO): ')

  nova_receita = Despesa(valor, categoria, descricao, forma_pagamento, 'despesa')
  nova_receita.salvarDespesa()