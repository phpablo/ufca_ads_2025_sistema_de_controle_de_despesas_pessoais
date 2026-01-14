from database.database import lerJsonCategorias
from database.database import salvarJsonCategorias

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

    @staticmethod
    def verificar_nome(self):
        categoriasCriadas = lerJsonCategorias()
        for i in categoriasCriadas:
            if i['nome'] == self.nome and i['tipo'] == self.tipo:
                return True
        return False
    
    @staticmethod    
    def criarCategoria(self):  
        categoriasCriadas = lerJsonCategorias()       
        if self.verificar_nome(self) is False:  
            dictCategoria = {
            "nome": self.nome,
            "tipo": self.tipo,
            "limite_mensal": self.limite_mensal,
            "descricao": self.descricao,
        }   
            categoriasCriadas.append(dictCategoria)
            salvarJsonCategorias(categoriasCriadas)
                  
        else:
            raise ValueError('Categoria duplicada') 
        
    @staticmethod        
    def excluirCategoria(nome, tipo):
        categoriasCriadas = lerJsonCategorias()
        for i in categoriasCriadas:
            if i['nome'] == nome and i['tipo'] == tipo.lower():
                categoriasCriadas.remove(i)
                salvarJsonCategorias(categoriasCriadas)
                return            
        raise ValueError('Categoria não encontrada')


    @staticmethod
    def editarCategoria(nome, campo, novo_valor):
        categoriasCriadas = lerJsonCategorias()
        tipo_aceito = ('receita', 'despesa') 
        for i in categoriasCriadas: 
            if i['nome'] == nome: 
                categoria_editada = i 
                categoriasCriadas.remove(i)
                break  
        else:
            raise ValueError('Categoria não encontrada')            
                    
        if campo.lower() == 'nome': 
            if not novo_valor.strip(): 
                raise ValueError('O campo novo valor deve ser preenchido')
            for j in categoriasCriadas: 
                if j['nome'] == novo_valor and j['tipo'] == categoria_editada['tipo']: 
                    raise ValueError('Categoria duplicada')         
            categoria_editada['nome'] = novo_valor
            categoriasCriadas.append(categoria_editada)
            salvarJsonCategorias(categoriasCriadas)

        if campo.lower() == 'tipo':
            if novo_valor.lower() not in tipo_aceito:
                raise ValueError('Valor inválido, o tipo deve ser "receita" ou "despesa"')
            categoria_editada['tipo'] = novo_valor
            categoriasCriadas.append(categoria_editada)
            salvarJsonCategorias(categoriasCriadas)

        if campo.lower() == 'limite mensal':
            if not isinstance(novo_valor, (int, float)) or novo_valor < 0:
                raise ValueError('O limite mensal deve ser um número e positivo')
            categoria_editada['limite_mensal'] = novo_valor
            categoriasCriadas.append(categoria_editada)
            salvarJsonCategorias(categoriasCriadas)

        if campo.lower() == 'descrição':
            categoria_editada['descricao'] = novo_valor
            categoriasCriadas.append(categoria_editada)  
            salvarJsonCategorias(categoriasCriadas)  
        
        


    

         


































