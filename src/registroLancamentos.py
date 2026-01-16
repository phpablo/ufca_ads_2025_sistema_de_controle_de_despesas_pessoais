# from database.database import lerJsonLancamentos, salvarJsonLancamentos
from src.receita import Receita
from src.despesa import Despesa

def criarReceita():
  print('\nRegistrar receita no sistema')

  valor = input('Valor da receita: ')
  while True:
    if valor.isnumeric():
      valor = float(valor)
      break
    else:
      print('Digite um valor válido')
      valor = input('Valor da receita: ')
  
  categoria = input('Nome da receita: ')
  descricao = input('Descrição: ')
  forma_pagamento = input('Forma de pagamento (DINHEIRO, PIX, DEBITO, CREDITO): ').upper()
  while True:
    if forma_pagamento.isalpha() and forma_pagamento in ['DINHEIRO', 'PIX', 'DEBITO', 'CREDITO']:
      break
    else:
      forma_pagamento = input('Forma de pagamento (DINHEIRO, PIX, DEBITO, CREDITO): ').upper()

  nova_receita = Receita(valor, categoria, descricao, forma_pagamento, 'receita')
  nova_receita.salvarReceita()

def criarDespesa():
  print('\nRegistrar despesa no sistema')

  valor = input('Valor da despesa: ')
  while True:
    if valor.isnumeric():
      valor = float(valor)
      break
    else:
      print('Digite um valor válido')
      valor = input('Valor da despesa: ')

  categoria = input('Nome da despesa: ')
  descricao = input('Descrição: ')
  forma_pagamento = input('Forma de pagamento (DINHEIRO, PIX, DEBITO, CREDITO): ')
  while True:
    if forma_pagamento.isalpha() and forma_pagamento in ['DINHEIRO', 'PIX', 'DEBITO', 'CREDITO']:
      break
    else:
      forma_pagamento = input('Forma de pagamento (DINHEIRO, PIX, DEBITO, CREDITO): ').upper()

  nova_receita = Despesa(valor, categoria, descricao, forma_pagamento, 'despesa')
  nova_receita.salvarDespesa()