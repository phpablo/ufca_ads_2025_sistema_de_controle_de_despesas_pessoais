# ======================================================================================================
# Universidade: Universidade Federal do Cariri (UFCA)
# Polo: Itapipoca-Ce
# Semestre: 2025.2
# Disciplina: Programação Orientada a Objetos
# Equipe 9: SARAH OLIVEIRA LUCAS DIÓGENES (2025013808)
#           SAULO VICTO SOARES (2025013853)
#           PABLO HENRIQUE LIMA DE ARAUJO (2025013700)
#           VINICIUS TABOSA DOS SANTOS (2025013890)
# Entregável 1
# ======================================================================================================

# Classes

## Lançamento (Sarah e Vinicius) 
### Atributos de Lançamento
- Valor
- Categoria
- Data
- Descrição
- Forma de pagamento

### Métodos de Lançamento
- Criar
- Editar
- Excluir
- Emitir alerta

## Categoria (Saulo)
### Atributos
- Nome
- Tipo
- Limite mensal
- Descrição (opcional)

### Métodos
- Relatório
- Emitir alerta

## Orçamento (Pablo)
### Atributo
- Orçamento total

### Método
- Calcular saldo diário
- Calcular saldo mensal
- Emitir alerta

## Receita (herda de Lançamento) (Sarah e Vinicius) 
### Métodos
- Relatório

## Despesa (herda de Lançamento) (Sarah e Vinicius) 
### Métodos
- Relatório

## Transferência (herda de Lançamento) (Saulo)
### Método
- Fazer transferência

## Alerta / Verificação (Pablo)
### Atributo
- Descrição

 ### Método
- Emitir alerta de alto valor
- Emitir alerta de limite de categoria
- Emitir alerta de déficit orçamentário

## Responsabilidade da Equipe
- Sarah e Vinicius: Responsáveis pela implementação da classe Lançamento e de suas subclasses
- Saulo: Responsável pela implementação da classe Categoria e Transferência
- Pablo: Responsável pela implementação da classe Orçamento e Alertas
