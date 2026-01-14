# 1. Cria a classe categoria com os 4 atributos principais. Também faz a validação inicial do preenchimento dos atributos
class Categoria: 
    def __init__(self, nome, tipo, limite_mensal, descricao):    
        tipo_aceito = ('receita', 'despesa')        
        if not nome.strip():
            raise ValueError('O campo nome deve ser preenchido')
        else:   
            self.nome = nome
        if tipo.lower() not in tipo_aceito:
            raise ValueError('Valor inválido, o tipo deve ser "receita" ou "despesa"')
        else:
            self.tipo = tipo.lower()
        if not isinstance(limite_mensal, (int, float)) or limite_mensal < 0:
            raise ValueError('O limite mensal deve ser um número e positivo')
        else:
            self.limite_mensal = limite_mensal
        self.descricao = descricao


# 2. Cria uma classe de gerenciamento que armazena todas as categorias criadas. Armazena também os métodos de manipulação das categorias

class GerenciarCategorias():    
    def __init__(self):      
        self.categorias_criadas = []  

    def verificar_nome(self, nome, tipo):
        for i in self.categorias_criadas:
            if i.nome == nome and i.tipo == tipo:
                return True
        return False
    
    def criarCategoria(self, Categoria):  
        if self.verificar_nome(Categoria.nome, Categoria.tipo) is False: 
            self.categorias_criadas.append(Categoria)   
        else:
            raise ValueError('Categoria duplicada') 
        
    def excluirCategoria(self, nome, tipo):
        for i in self.categorias_criadas:
            if i.nome == nome and i.tipo == tipo.lower():
                self.categorias_criadas.remove(i)
                return            
        raise ValueError('Categoria não encontrada')
    
    def editarCategoria(self, nome, campo, novo_valor):
        tipo_aceito = ('receita', 'despesa') 
        for i in self.categorias_criadas: #
            if i.nome == nome: 
                self.categoria_editada = i 
                self.categorias_criadas.remove(i)
                break  
        else:
            raise ValueError('Categoria não encontrada')            
                    
        if campo.lower() == 'nome': 
            if not novo_valor.strip(): 
                raise ValueError('O campo nome deve ser preenchido')
            
            for j in self.categorias_criadas: 
                if j.nome == novo_valor and j.tipo == self.categoria_editada.tipo: 
                    raise ValueError('Categoria duplicada')           
            
            self.categoria_editada.nome = novo_valor
            self.categorias_criadas.append(self.categoria_editada)

        if campo.lower() == 'tipo':
            if novo_valor.lower() not in tipo_aceito:
                raise ValueError('Valor inválido, o tipo deve ser "receita" ou "despesa"')
            self.categoria_editada.tipo = novo_valor
            self.categorias_criadas.append(self.categoria_editada)

        if campo.lower() == 'limite mensal':
            if not isinstance(novo_valor, (int, float)) or novo_valor < 0:
                raise ValueError('O limite mensal deve ser um número e positivo')
            self.categoria_editada.limite_mensal = novo_valor
            self.categorias_criadas.append(self.categoria_editada)

        if campo.lower() == 'descrição':
            self.categoria_editada.descricao = novo_valor
            self.categorias_criadas.append(self.categoria_editada)    
         


































