# 💰 Sistema de Controle Financeiro Pessoal

> **Entregável 1** - Disciplina de Programação Orientada a Objetos (POO)

Este projeto consiste no desenvolvimento de um sistema para gestão de finanças pessoais. O objetivo é aplicar conceitos fundamentais de Orientação a Objetos, como herança, encapsulamento e divisão de responsabilidades, para criar uma ferramenta capaz de gerenciar receitas, despesas, orçamentos e emitir alertas financeiros.

---

## 🏫 Informações Acadêmicas

| Instituição | **Universidade Federal do Cariri (UFCA)** |
| :--- | :--- |
| **Polo** | Itapipoca-CE |
| **Semestre** | 2025.2 |
| **Disciplina** | Programação Orientada a Objetos |
| **Equipe** | 09 |

### 👥 Integrantes da Equipe

| Nome | Matrícula | Função Principal |
| :--- | :--- | :--- |
| **Sarah Oliveira Lucas Diógenes** | 2025013808 | Implementação (Lançamentos/Subclasses) |
| **Saulo Victo Soares** | 2025013853 | Implementação (Categorias/Interface) |
| **Pablo Henrique Lima de Araujo** | 2025013700 | Implementação (Orçamento/Alertas/Dados) |
| **Vinicius Tabosa dos Santos** | 2025013890 | Implementação (Lançamentos/Subclasses) |

---

## 🛠️ Arquitetura do Projeto

O sistema foi modelado com base nas seguintes classes e responsabilidades:

### 1. Classe Base: Lançamento
Classe "mãe" que define a estrutura básica de qualquer movimentação financeira.
* **Atributos:**
    * `Valor` (Monetário)
    * `Categoria` (Associação)
    * `Data` (Data do evento)
    * `Descrição` (Texto)
    * `Forma de pagamento` (Enum/Tipo)
* **Métodos:**
    * `Criar()`, `Editar()`, `Excluir()`
    * `Emitir alerta()`

### 2. Subclasses (Herança de Lançamento)
Especializações da classe Lançamento.

* **📈 Receita:**
    * *Métodos Específicos:* `Relatório()`
* **📉 Despesa:**
    * *Métodos Específicos:* `Relatório()`


### 3. Classe: Categoria
Responsável por tipificar os lançamentos e definir tetos de gastos.
* **Atributos:**
    * `Nome`, `Tipo`, `Limite mensal`, `Descrição (opcional)`
* **Métodos:**
    * `Relatório()`
    * `Emitir alerta()`

### 4. Classe: Orçamento
Gerencia o saldo global e cálculos periódicos.
* **Atributos:**
    * `Orçamento total`
* **Métodos:**
    * `Calcular saldo diário()`
    * `Calcular saldo mensal()`
    * `Emitir alerta()`

### 5. Classe: Alerta / Verificação
Sistema de monitoramento e notificações de saúde financeira.
* **Atributos:**
    * `Descrição`
* **Métodos:**
    * `Emitir alerta de alto valor`
    * `Emitir alerta de limite de categoria`
    * `Emitir alerta de déficit orçamentário`

---

## 📅 Divisão de Responsabilidades

A execução do projeto foi dividida entre os membros da equipe para garantir a cobertura de todas as funcionalidades propostas no Entregável 1:

* **Sarah e Vinicius:**
    * Implementação completa da classe **Lançamento**.
    * Implementação das subclasses: **Receita** e **Despesa**.
* **Saulo:**
    * Implementação da classe **Categoria**.
    * Implementação da classe **Transferência** (herda de Lançamento).
    * Desenvolvimento da **Interface de Usuário (Console)**.
* **Pablo:**
    * Implementação da classe **Orçamento**.
    * Implementação da lógica de **Alertas/Verificação**.
    * Responsável pelo sistema de **Armazenamento de Dados**.

---

<div align="center">
  <sub>UFCA - Campus Itapipoca | 2025</sub>
</div>