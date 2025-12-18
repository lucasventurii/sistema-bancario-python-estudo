from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual, Agencia


def main():
    # Criando uma conta corrente para o cliente Lucas
    conta_lucas = ContaCorrente('Lucas', '123.456.789-00', '0001', '12345-6')

    # Criando um cartão de crédito vinculado à conta do Lucas
    cartao_lucas = CartaoCredito('Lucas', conta_lucas)

    # Criando diferentes tipos de agências
    agencia_comum = AgenciaComum('(11)556645', '1378667632/0001')
    agencia_premium = AgenciaPremium('(11)5534545', '135667632/0001')
    agencia_virtual = AgenciaVirtual(
        'www.agenciavirtual.com.br', '(11)5534545', '143426/0001')

    # Adicionando clientes às agências
    agencia_comum.adicionar_cliente('Lucas', '123.456.789-00', 3000)
    agencia_premium.adicionar_cliente('Carlos', '987.654.321-00', 6000)

    # Verificando o caixa das agências
    agencia_comum.verificar_caixa()
    agencia_premium.verificar_caixa()
    agencia_virtual.verificar_caixa()

    # Realizando algumas transações bancárias
    print("\n>>> Realizando Transações de Conta Corrente:")
    conta_lucas.depositar(1500)
    conta_lucas.consultar_saldo()
    conta_lucas.sacar_dinheiro(500)
    conta_lucas.consultar_saldo()

    # Transferindo dinheiro para outra conta
    conta_destino = ContaCorrente('Maria', '987.654.321-00', '0002', '54321-0')
    conta_lucas.transferir(300, conta_destino)
    print(f"\n>>> Saldo após transferência:")
    conta_lucas.consultar_saldo()
    conta_destino.consultar_saldo()

    # Exibindo informações do cartão de crédito
    print("\n>>> Informações do Cartão de Crédito:")
    print(f"Titular: {cartao_lucas.titular}")
    print(f"Número do Cartão: {cartao_lucas.numero}")
    print(f"Validade: {cartao_lucas.validade}")
    print(f"Código de Segurança: {cartao_lucas.cod_seguranca}")

    # Alterando a senha do cartão de crédito
    cartao_lucas.senha = '9876'
    print(f"Nova senha do cartão: {cartao_lucas.senha}")

    # Exibindo as transações da conta de Lucas
    print("\n>>> Histórico de Transações da Conta do Lucas:")
    conta_lucas.consultar_historico()


if __name__ == "__main__":
    main()
