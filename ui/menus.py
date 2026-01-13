from ui.leitura import ler_opcao

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


def MenuPrincipal(): 
    while True:
        print('- 1. Gerenciar Categorias')
        print('- 2. Gerenciar Lançamentos')
        print('- 3. Relatórios')
        print('- 0. Sair')
        opcao = ler_opcao()
        if opcao == 0:
            break
        elif opcao == 1:
            MenuCategorias()
        # else:
        #     print('Opção inválida')





