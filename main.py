from src.orcamento import Orcamento
from src.lancamento import Lancamento
from src.categoria import Categoria, GerenciarCategorias

def  main():
    orcamento = Orcamento(5000)
    casa = Categoria('Casa', 'despesa', 1000, 'Despesas de casa')
    categorias = GerenciarCategorias()
    categorias.criarCategoria(casa)
    categorias.excluirCategoria(casa.nome, casa.tipo)


if __name__ == '__main__':
    main()