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
        
        try:
            limite_mensal = float(limite_mensal)
        except:
            raise ValueError('O limite mensal deve ser um número')
    
        if limite_mensal < 0:
            raise ValueError('O limite mensal deve ser positivo')
        
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
            categoria_editada['tipo'] = novo_valor.lower()
            categoriasCriadas.append(categoria_editada)
            salvarJsonCategorias(categoriasCriadas)

        if campo.lower() == 'limite mensal':
            try:
                novo_valor = float(novo_valor)
            except:
                raise ValueError('O novo campo de limite mensal deve ser um número')
            if novo_valor < 0:
                raise ValueError('O valor de limite mensal deve ser positivo')
            categoria_editada['limite_mensal'] = novo_valor
            categoriasCriadas.append(categoria_editada)
            salvarJsonCategorias(categoriasCriadas)

        if campo.lower() == 'descrição':
            categoria_editada['descricao'] = novo_valor
            categoriasCriadas.append(categoria_editada)  
            salvarJsonCategorias(categoriasCriadas)  

    @staticmethod
    def listarCategorias():
        categoriasCriadas = lerJsonCategorias()
        if len(categoriasCriadas) == 0:
            raise ValueError('Nenhuma categoria cadastrada')
        else:
            for i in categoriasCriadas:
                nome = i['nome']
                tipo = i['tipo']
                limiteMensal = i['limite_mensal']
                descricao = i['descricao']
                print(f'{nome} || {tipo} || {limiteMensal} || {descricao}')
                print(len(f'{nome} || {tipo} || {limiteMensal} || {descricao}')*'-')
  
    
        
        


    

         


































