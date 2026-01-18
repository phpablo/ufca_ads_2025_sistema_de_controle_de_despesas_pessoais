import os
from src.categoria import Categoria
from src.registroLancamentos import criarDespesa, criarReceita
from src.orcamento import Orcamento


class MenuPrincipal:
    def __init__(self):
        pass

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def iniciar(self):
        self.limpar_tela()
        print("=" * 40)
        print("SISTEMA DE CONTROLE FINANCEIRO")
        print("=" * 40)
        while True:
            print('1 - Gerenciar Categorias')
            print('2 - Lançar Receita')
            print('3 - Lançar Despesa')
            print('4 - Ver Saldo')
            print('5 - Ver Relatórios')
            print('0 - Sair')
            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                opCategoria = self.menuCategoria()

            elif opcao == '2':
                try:
                    self.limpar_tela()
                    print('--- Criar Receita ---') 
                    opReceita = criarReceita()
                except ValueError as e:
                    print(f'Erro: {e}')

            elif opcao == '3':
                try:
                    self.limpar_tela()
                    print('--- Criar Despesa ---') 
                    opDespesa = criarDespesa()
                except ValueError as e:
                    print(f'Erro: {e}')

            elif opcao == '4':
                opSaldo = self.menuOrcamento()
                
            elif opcao == '0':
                self.limpar_tela()
                print('Saindo do sistema...')
                break
            
    def menuCategoria(self):
        self.limpar_tela()
        print('--- Gerencia de Categorias ---')        
        while True:
            print('1 - Listar Categorias')
            print('2 - Criar Categoria')
            print('3 - Remover Categoria')
            print('4 - Editar Categoria')
            print('0 - Retornar para o menu principal')
            opcao = input('Escolha uma opção: ')
            self.limpar_tela()

            if opcao == '1':
                self.limpar_tela()
                print(' -- Lista de Categorias Criadas -- ')
                print('Nome || Tipo || Limite Mensal || Descrição')
                print(len('Nome || Tipo || Limite Mensal || Descrição')*'-')
                try:
                    Categoria.listarCategorias()
                except ValueError as e:
                    print(f'Erro: {e}')

            elif opcao == '2':    
                try:            
                    nome = input('Digite o nome da categoria: ')
                    tipo = input('Digite o tipo da categoria (RECEITA OU DESPESA): ')                
                    limiteMensal = input('Digite o limite de gastos para essa categoria: ')
                    descricao = input('Faça uma descrição da categoria: ')                    
                    objCategoria = Categoria(nome, tipo, limiteMensal, descricao)
                    objCategoria.criarCategoria(objCategoria)
                    print('Categoria criada com sucesso')
                    self.limpar_tela()

                except ValueError as e:
                    print(f'Erro: {e}')  
                
            elif opcao == '3':
                nome = input('Digite o nome da categoria que deseja excluir (lembre de escrever conforme foi cadastrada): ')
                tipo = input('Digite o tipo da categoria que deseja excluir (RECEITA OU DESPESA): ')
                try:
                    Categoria.excluirCategoria(nome, tipo)
                except ValueError as e:
                    print(f'Erro: {e}')
                    
            elif opcao == '4':
                nome = input('Digite o nome da categoria que deseja editar (lembre de escrever conforme foi cadastrada): ')
                campo = input('Digite o campo que deseja editar (OPÇÔES: nome, tipo, limite mensal, descrição): ')
                novoValor = input('Digite o novo valor do campo: ')
                try:
                    Categoria.editarCategoria(nome, campo, novoValor)
                except ValueError as e:
                    print(f'Erro: {e}')
                
            elif opcao == '0':
                break
        
    def menuOrcamento(self):
        self.limpar_tela()
        print('--- Calcular Saldo ---') 
        objOrcamento = Orcamento()
        saldo, receita, despesa = objOrcamento.saldoGlobal()
        print(f'Saldo Atual: R$ {saldo}')
        print(f'Total de despesas: R$ {despesa}')
        print(f'Total de receitas: R$ {receita}')        
        print('1 - Calcular Saldo Mensal')
        print('2 - Calcular Saldo Diário')
        print('0 - Voltar para o menu principal')
        opcao = input('Escolha uma opção: ')
        while True:            
            if opcao == '1':
                mes = input('Digite o número relativo ao mês (ex: 1 - janeiro): ')
                ano = input('ano de referência: ')
                saldoMensal = Orcamento()
                print(f'O saldo mensal para o mês é: {saldoMensal.calcular_saldo_mensal(mes, ano)}')                             
                break
            elif opcao == '2':
                dia = input('Digite o número relativo ao dia: ')
                mes = input('Digite o número relativo ao mês (ex: 1 - janeiro): ')
                ano = input('ano de referência: ')
                saldoMensal = Orcamento()
                print(f'O saldo mensal para o dia escolhido é: {saldoMensal.calcular_saldo_diario(dia, mes, ano)}')                             
                break
            elif opcao == '3':
                break









        
        

