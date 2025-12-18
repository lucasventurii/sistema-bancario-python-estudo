from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Classe que representa uma conta corrente de um cliente.
    Permite realizar depósitos, saques, transferências, consultar saldo e histórico de transações.
    """

    @staticmethod
    def _data_hora():
        """
        Retorna a data e hora no fuso horário de São Paulo (Brasil).
        """
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, conta):
        """
        Inicializa uma conta corrente para um cliente com informações básicas.
        
        :param nome: Nome do titular da conta
        :param cpf: CPF do titular da conta
        :param agencia: Número da agência
        :param conta: Número da conta
        """
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0  # Saldo inicial
        self.limite = None  # Limite da conta (ainda não definido)
        self.agencia = agencia
        self.conta = conta
        self.transacoes = []  # Lista de transações realizadas
        self.cartoes = []  # Lista de cartões vinculados à conta

    def consultar_saldo(self):
        """
        Exibe o saldo atual da conta.
        """
        print(f'O seu saldo é de R$ {self.saldo:,.2f}')

    def depositar(self, valor):
        """
        Realiza o depósito de um valor na conta.
        
        :param valor: Valor a ser depositado
        """
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(
                (valor, self.saldo, ContaCorrente._data_hora()))
            print(f'Depósito de R$ {valor:,.2f} realizado com sucesso.')
        else:
            print("Valor inválido para depósito.")

    def _limite_conta(self):
        """
        Define o limite da conta, se necessário.
        O limite é fixado em R$ -1000,00 para saques.
        """
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        """
        Realiza o saque de um valor da conta, verificando se o saldo é suficiente.
        
        :param valor: Valor a ser sacado
        """
        if valor > 0 and self.saldo - valor >= self._limite_conta():
            self.saldo -= valor
            self.transacoes.append(
                (-valor, self.saldo, ContaCorrente._data_hora()))
            print(f'Saque de R$ {valor:,.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente para saque.')

    def consultar_limite(self):
        """
        Exibe o limite disponível na conta.
        """
        print(f'O seu limite é de R$ {self.limite:,.2f}')

    def consultar_historico(self):
        """
        Exibe o histórico de transações da conta.
        """
        print('Histórico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(
                f'R$ {transacao[0]:,.2f} | Saldo: R$ {transacao[1]:,.2f} | Data: {transacao[2]}')

    def transferir(self, valor, conta_destino):
        """
        Realiza a transferência de um valor para outra conta.
        
        :param valor: Valor a ser transferido
        :param conta_destino: Conta de destino para a transferência
        """
        if valor > 0 and self.saldo - valor >= self._limite_conta():
            self.saldo -= valor
            conta_destino.saldo += valor
            self.transacoes.append(
                (-valor, self.saldo, ContaCorrente._data_hora()))
            conta_destino.transacoes.append(
                (valor, conta_destino.saldo, ContaCorrente._data_hora()))
            print(
                f'Transferência de R$ {valor:,.2f} realizada para a conta {conta_destino.conta}.')
        else:
            print('Transferência não realizada. Verifique o valor ou saldo insuficiente.')


class CartaoCredito:
    """
    Classe que representa um cartão de crédito vinculado a uma conta corrente.
    Permite definir o limite do cartão, a senha e validar as informações.
    """

    @staticmethod
    def _data_hora():
        """
        Retorna a data e hora no fuso horário de São Paulo (Brasil).
        """
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        """
        Inicializa um cartão de crédito vinculado a uma conta corrente.
        
        :param titular: Nome do titular do cartão
        :param conta_corrente: Conta corrente vinculada ao cartão
        """
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 7}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000  # Limite inicial do cartão
        self._senha = '12345'  # Senha inicial do cartão
        self.conta_corrente = conta_corrente
        # Vincula o cartão à conta corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        """
        Retorna a senha do cartão de crédito.
        """
        return self._senha

    @senha.setter
    def senha(self, valor):
        """
        Define a nova senha do cartão, verificando se a senha é válida (4 dígitos numéricos).
        
        :param valor: Nova senha a ser definida
        """
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print(f'Senha do cartão alterada para: {self._senha}')
        else:
            print('Nova senha inválida. A senha deve conter 4 dígitos numéricos.')


# Exemplo de como as classes funcionam:

if __name__ == "__main__":
    # Criando uma conta para o cliente Lucas
    conta_lucas = ContaCorrente('Lucas', '123.456.789-00', '0001', '12345-6')

    # Criando um cartão de crédito vinculado à conta de Lucas
    cartao_lucas = CartaoCredito('Lucas', conta_lucas)

    # Realizando algumas transações na conta de Lucas
    conta_lucas.depositar(1000)
    conta_lucas.sacar_dinheiro(500)
    conta_lucas.consultar_saldo()

    # Realizando uma transferência para outra conta
    conta_maria = ContaCorrente('Maria', '987.654.321-00', '0002', '54321-0')
    conta_lucas.transferir(200, conta_maria)

    # Consultando o histórico de transações de Lucas
    conta_lucas.consultar_historico()

    # Modificando a senha do cartão de crédito de Lucas
    cartao_lucas.senha = '9876'
