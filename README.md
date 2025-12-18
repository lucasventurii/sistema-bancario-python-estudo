# 💳 Banco Digital em Python 🏦

Este projeto é uma simulação de um sistema bancário em Python. Ele possui classes para **contas correntes**, **cartões de crédito**, **agências bancárias** (comum, premium e virtual), além de funcionalidades como **depósitos**, **saques**, **transferências** e **empréstimos**. O sistema simula as principais operações bancárias e permite que os usuários interajam com diferentes tipos de agências.

## 🚀 Funcionalidades

### 🏦 **Agência Bancária**
- Adição de clientes 🧑‍🤝‍🧑
- Verificação do caixa da agência 💸
- Realização de empréstimos 💰

### 💳 **Conta Corrente**
- Depósitos 💵
- Saques 💳
- Transferências bancárias 💸
- Consulta de saldo 💲
- Histórico de transações 📜

### 💳 **Cartão de Crédito**
- Criação de um cartão de crédito vinculado à conta corrente 💳
- Alteração de senha do cartão 🔐
- Exibição das informações do cartão 💳

## 🧑‍💻 **Estrutura do Projeto**

### Arquivos:
- **`main.py`**: Arquivo principal para a execução do sistema bancário.
- **`ContasBancos.py`**: Contém as classes `ContaCorrente` e `CartaoCredito`.
- **`Agencia.py`**: Contém as classes `Agencia`, `AgenciaVirtual`, `AgenciaComum` e `AgenciaPremium`.

## 🛠️ **Tecnologias Utilizadas:**
- Python 3.x
- Biblioteca `pytz` para manipulação de datas e horas no fuso horário de São Paulo.
- Biblioteca `random` para geração de números aleatórios (como número da conta e do cartão de crédito).

## 🖼️ **Diagrama de Classes**

Aqui está um diagrama simplificado da estrutura de classes:

              +--------------------+
              |      Agencia       |
              +--------------------+
              | - telefone         |
              | - cnpj             |
              | - numero           |
              | - caixa            |
              +--------------------+
              | + verificar_caixa() |
              | + emprestar_dinheiro()|
              | + adicionar_cliente()|
              +--------------------+
                      |
         +------------+------------+
         |                         |
+-------------------+      +-------------------+
|     Agencia      |      |   AgenciaComum    |
|     Virtual      |      |                   |
+-------------------+      +-------------------+
         |                         |
+-------------------+      +-------------------+
|    CartaoCredito  |      |   ContaCorrente   |
+-------------------+      +-------------------+



### 🎯 ** Objetivo do Projeto **

- O objetivo desse projeto é praticar a programação orientada a objetos em Python, criando um sistema bancário simples, mas que simula as operações essenciais de um banco. O projeto também visa entender como criar e gerenciar classes e objetos de forma eficiente.


