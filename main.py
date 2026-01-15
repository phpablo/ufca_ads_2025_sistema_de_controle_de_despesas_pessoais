from ui.menus import MenuPrincipal
from src.categoria import Categoria
from src.despesa import Despesa

# if __name__ == '__main__':
#     categoriaTeste = Categoria('Teste', 'Despesa', 1500, 'Despesas com coisas de casa')
#     categoriaTeste.criarCategoria(categoriaTeste)
    

if __name__ == '__main__':
    print('='*150)
    print(' '* 55 + 'SISTEMA DE CONTROLE DE DESPESAS PESSOAIS')
    print('='*150)
    print(' '*11 + 'Instruções de uso: siga as instruções do terminal. Para a indicar a operação, seleciona o número associado e confirme o comando')
    print(' '*57 + 'Escolha uma das opções a seguir:\n')
    MenuPrincipal()


