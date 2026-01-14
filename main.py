from ui.menus import MenuPrincipal
from src.lancamento import Lancamento
from src.categoria import Categoria

if __name__ == '__main__':
    casa = Categoria('Casa', 'Despesa', 500, 'Despesas com coisas de casa')
    salario = Categoria('Salário', 'Receita', 4500, 'Salário empresa')
    compras = Categoria('Mercado', 'Despesa', 1500, 'Despesa com mercado')


    # Categoria.criarCategoria(casa)
    # Categoria.criarCategoria(salario)
    # Categoria.criarCategoria(compras)

    Categoria.editarCategoria('Despesa de casa', 'descrição', 'Teste de nova descrição')
    
    


    


# if __name__ == '__main__':
#     print('='*150)
#     print(' '* 55 + 'SISTEMA DE CONTROLE DE DESPESAS PESSOAIS')
#     print('='*150)
#     print(' '*11 + 'Instruções de uso: siga as instruções do terminal. Para a indicar a operação, seleciona o número associado e confirme o comando')
#     print(' '*57 + 'Escolha uma das opções a seguir:')
#     MenuPrincipal()


