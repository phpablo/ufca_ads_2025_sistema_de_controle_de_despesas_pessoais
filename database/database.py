import json

def lerJsonCategorias():
    with open('./database/dataBaseCategorias.json', 'r') as arquivo:          
        return json.load(arquivo)  

def salvarJsonCategorias(jsonCategorias):
    with open('./database/dataBaseCategorias.json', 'w') as arquivo:
        json.dump(jsonCategorias, arquivo, ensure_ascii=False, indent=2)
    
def lerJsonLancamentos():
    with open('./database/dataBaseLancamentos.json', 'r') as arquivo:
        return json.load(arquivo)

def salvarJsonLancamentos(dictReceita):
    with open('./database/dataBaseLancamentos.json', 'w') as arquivo:
        json.dump(dictReceita, arquivo, ensure_ascii=False, indent=2)
        
def lerJsonSettings():
    with open('./database/settings.json', 'r') as arquivo:
        return json.load(arquivo)
print("database.py carregado com sucesso")
    


