from ui.leitura import ler_opcao
from src.registroLancamentos import criarDespesa, criarReceita
from database.database import lerJsonSettings

def MenuCategorias():
    print(' '*65 + 'C A T E G O R I A S')
    while True:
        print('- 1. Cadastrar Categorias')
        print('- 2. Listar Categorias')
        print('- 3. Editar Categoria')
        print('- 4. Remover Categoria')
        print('- 0. Voltar')
        opcao = ler_opcao()

        if opcao == 0:
            return

def menuLancamentos():
    print(' '*65 + 'L A N Ç A M E N T O S')
    while True:
        print('\n- 1. Registrar receita')
        print('- 2. Registrar despesa')
        print('- 0. Sair')
        opcao = ler_opcao()
        if opcao == 0:
            break
        elif opcao == 1:
            criarReceita()
        elif opcao == 2:
            criarDespesa()

def menuConfiguracoes():
    print(' '*65 + 'C O N F I G U R A Ç Õ E S')
    print('-1. Ver configurações de alertas')
    print('-2. Ver configurações de relatórios')
    print('-3. Ver configurações de orçamento')
    print('-4. Ver validações do sistema')
    print('- 0. Sair')
    opcao = ler_opcao()
    if opcao == 0:
        return
    settings = lerJsonSettings()

    if opcao == 1:
        print('\n ALERTAS')
        print(f"- Valor para alerta de alto gasto: R$ {settings['alertas']['alto_valor_de_despesa']:.2f}")
        print(f"- Alerta de limite por categoria: {settings['alertas']['ativar_alerta_limite_categoria']}")
        print(f"- Alerta de saldo negativo: {settings['alertas']['ativar_alerta_saldo_negativo']}")
    
    elif opcao == 2:
        print('\n RELATÓRIOS')
        print(f"- Meses para comparativo: R$ {settings['relatorios']['meses_comparativos']}")
        print(f"- Alerta de limite por categoria: {settings['alertas']['ativar_alerta_limite_categoria']}")
        print(f"- Alerta de saldo negativo: {settings['alertas']['ativar_alerta_saldo_negativo']}")

    elif opcao == 3:
        print('\n ORÇAMENTO')
        print(f"- Meta mensal de economia: {settings['orcamento']['percentual_meta_economia']*100.0: .0f}%")

    elif opcao == 4:
        print('\n VALIDACOES')
        print(f"- Valor mínimo por lançamento: R$ {settings['validacoes']['valor_minimo_lancamento']:.2f}")
        

def MenuPrincipal(): 
    while True:
        print(' '*65 + 'M E N U')
        print('- 1. Gerenciar Categorias')
        print('- 2. Gerenciar Lançamentos')
        print('- 3. Configurações')
        print('- 4. Relatórios')
        print('- 0. Sair')
        opcao = ler_opcao()
        if opcao == 0:
            break
        elif opcao == 1:
            MenuCategorias()
        elif opcao == 2:
            menuLancamentos()
        elif opcao == 3:
            menuConfiguracoes()
        # else:
        #     print('Opção inválida')





