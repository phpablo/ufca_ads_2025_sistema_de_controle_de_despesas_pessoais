## Classes

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
