from random import randint


class Agencia:
    """
    Classe que representa uma agência bancária genérica.
    Possui funcionalidades de verificação do caixa, concessão de empréstimos e adição de clientes.
    """

    def __init__(self, telefone, cnpj, numero):
        """
        Inicializa uma instância da agência com informações básicas.
        
        :param telefone: Número de telefone da agência
        :param cnpj: CNPJ da agência
        :param numero: Número da agência
        """
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []  # Lista de clientes da agência
        self.caixa = 0  # Caixa inicial da agência
        self.emprestimos = []  # Lista de empréstimos realizados

    def verificar_caixa(self):
        """
        Verifica o valor do caixa da agência e emite um aviso caso o caixa esteja abaixo do recomendado.
        """
        if self.caixa < 1000:
            print(
                f'Caixa abaixo do nível recomendado. Caixa atual: R$ {self.caixa:,.2f}')
        else:
            print(
                f'O valor de caixa está ok. Caixa atual: R$ {self.caixa:,.2f}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        """
        Realiza o empréstimo de dinheiro, caso haja caixa suficiente.
        
        :param valor: Valor do empréstimo
        :param cpf: CPF do cliente solicitante
        :param juros: Taxa de juros aplicada ao empréstimo
        """
        if self.caixa >= valor:
            # Registra o empréstimo com o valor, CPF do cliente e juros aplicados
            self.emprestimos.append((valor, cpf, juros))
            print(
                f'Empréstimo de R$ {valor:,.2f} concedido a {cpf} com {juros}% de juros.')
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        """
        Adiciona um cliente à agência, caso o patrimônio seja suficiente.
        
        :param nome: Nome do cliente
        :param cpf: CPF do cliente
        :param patrimonio: Patrimônio do cliente
        """
        if patrimonio >= 1000:
            self.clientes.append((nome, cpf, patrimonio))
            print(f'Cliente {nome} adicionado com sucesso.')
        else:
            print(
                'O cliente não tem o patrimônio necessário para se tornar um cliente da agência.')

    def exibir_informacoes_agencia(self):
        """
        Exibe informações básicas da agência, como número, telefone e CNPJ.
        """
        print(
            f"Agência {self.numero} - Telefone: {self.telefone} - CNPJ: {self.cnpj}")


class AgenciaVirtual(Agencia):
    """
    Representa uma agência virtual com funcionalidades específicas.
    Herda da classe Agência e permite transações em PayPal.
    """

    def __init__(self, site, telefone, cnpj):
        """
        Inicializa a agência virtual com informações adicionais.
        
        :param site: URL do site da agência virtual
        :param telefone: Número de telefone da agência
        :param cnpj: CNPJ da agência
        """
        self.site = site
        super().__init__(telefone, cnpj, 1000)  # Número da agência virtual fixo
        self.caixa = 1500  # Caixa inicial para a agência virtual
        self.caixa_paypal = 0  # Caixa do PayPal da agência virtual

    def depositar_paypal(self, valor):
        """
        Deposita um valor no caixa do PayPal da agência virtual.
        
        :param valor: Valor a ser depositado no PayPal
        """
        if valor > 0:
            self.caixa -= valor
            self.caixa_paypal += valor
            print(f'Depósito de R$ {valor:,.2f} realizado no PayPal.')
        else:
            print('Valor de depósito inválido.')

    def sacar_paypal(self, valor):
        """
        Realiza um saque do PayPal para o caixa da agência virtual.
        
        :param valor: Valor a ser sacado do PayPal
        """
        if valor <= self.caixa_paypal:
            self.caixa_paypal -= valor
            self.caixa += valor
            print(
                f'Saque de R$ {valor:,.2f} realizado do PayPal para o caixa.')
        else:
            print('Saldo insuficiente no PayPal para saque.')

    def exibir_informacoes_agencia(self):
        """
        Exibe as informações específicas da agência virtual, incluindo o site.
        """
        print(
            f"Agência Virtual - Site: {self.site} - Telefone: {self.telefone} - CNPJ: {self.cnpj}")


class AgenciaComum(Agencia):
    """
    Representa uma agência bancária comum, com caixa padrão.
    """

    def __init__(self, telefone, cnpj):
        """
        Inicializa uma agência comum com um caixa inicial fixo.
        
        :param telefone: Número de telefone da agência
        :param cnpj: CNPJ da agência
        """
        super().__init__(telefone, cnpj, randint(1001, 9999)
                         )  # Número da agência comum gerado aleatoriamente
        self.caixa = 1800  # Caixa inicial para a agência comum


class AgenciaPremium(Agencia):
    """
    Representa uma agência premium, que oferece serviços exclusivos para clientes com maior patrimônio.
    """

    def __init__(self, telefone, cnpj):
        """
        Inicializa uma agência premium com um caixa inicial mais alto.
        
        :param telefone: Número de telefone da agência
        :param cnpj: CNPJ da agência
        """
        super().__init__(telefone, cnpj, randint(1001, 9999)
                         )  # Número da agência premium gerado aleatoriamente
        self.caixa = 2500  # Caixa inicial para a agência premium

    def adicionar_cliente(self, nome, cpf, patrimonio):
        """
        Adiciona um cliente à agência premium somente se ele atender ao requisito de patrimônio.
        
        :param nome: Nome do cliente
        :param cpf: CPF do cliente
        :param patrimonio: Patrimônio do cliente
        """
        if patrimonio > 5000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print(
                'O cliente não tem o patrimônio necessário para se tornar um cliente premium.')


# Exemplo de uso

agencia_comum = AgenciaComum('(11)556645', '1378667632/0001')
agencia_comum.adicionar_cliente('Lucas', '123.456.789-00', 3000)
agencia_comum.verificar_caixa()

agencia_virtual = AgenciaVirtual(
    'www.agenciavirtual.com.br', '(11)5534545', '143426/0001')
agencia_virtual.depositar_paypal(500)
agencia_virtual.sacar_paypal(100)
agencia_virtual.exibir_informacoes_agencia()

agencia_premium = AgenciaPremium('(11)5534545', '135667632/0001')
agencia_premium.adicionar_cliente('Carlos', '987.654.321-00', 6000)
agencia_premium.verificar_caixa()
