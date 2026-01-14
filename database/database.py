import json

def lerJsonCategorias():
    with open('./database/dataBaseCategorias.json', 'r') as arquivo:          
        return json.load(arquivo)  

def salvarJsonCategorias(jsonCategorias):
    with open('./database/dataBaseCategorias.json', 'w') as arquivo:
        json.dump(jsonCategorias, arquivo, ensure_ascii=False, indent=2)
    



    


