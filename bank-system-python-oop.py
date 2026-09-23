# CLASSE CONTA BANCÁRIA

class ContaBancaria:

    # Método construtor da classe
    # Executa automaticamente quando um objeto é criado
    def __init__(self, titular, numero_conta, saldo=0):

        # Atributos da conta
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

        # Lista que armazenará movimentações da conta
        self.extrato = []

    # MÉTODO DE DEPÓSITO

    def depositar(self, valor_deposito):

        # Verifica se valor é válido
        if valor_deposito <= 0:
            print("❌ Digite um valor válido para depósito.")
            return

        # Soma valor ao saldo
        self.saldo += valor_deposito

        # Salva movimentação no extrato
        self.extrato.append(
            f"Depósito realizado: +R$ {valor_deposito:.2f}"
        )

        print("✅ Depósito realizado com sucesso!")

    # MÉTODO DE SAQUE

    def sacar(self, valor_saque):

        # Verifica se valor é válido
        if valor_saque <= 0:
            print("❌ Digite um valor válido para saque.")
            return

        # Verifica se saldo é suficiente
        if valor_saque > self.saldo:
            print("❌ Saldo insuficiente.")
            return

        # Remove valor do saldo
        self.saldo -= valor_saque

        # Adiciona movimentação ao extrato
        self.extrato.append(
            f"Saque realizado: -R$ {valor_saque:.2f}"
        )

        print("✅ Saque realizado com sucesso!")

    # MÉTODO PARA MOSTRAR SALDO

    def mostrar_saldo(self):

        print(f"""
=========================
Titular: {self.titular}
Conta: {self.numero_conta}
Saldo: R$ {self.saldo:.2f}
=========================
""")

    # MÉTODO DE TRANSFERÊNCIA

    def transferir(self, valor_transferencia, conta_destino):

        # Verifica valor válido
        if valor_transferencia <= 0:
            print("❌ Digite um valor válido.")
            return

        # Verifica saldo disponível
        if valor_transferencia > self.saldo:
            print("❌ Saldo insuficiente.")
            return

        # Remove valor da conta origem
        self.saldo -= valor_transferencia

        # Adiciona valor na conta destino
        conta_destino.saldo += valor_transferencia

        # Adiciona movimentação no extrato da conta origem
        self.extrato.append(
            f"Transferência enviada para "
            f"{conta_destino.titular}: "
            f"-R$ {valor_transferencia:.2f}"
        )

        # Adiciona movimentação no extrato da conta destino
        conta_destino.extrato.append(
            f"Transferência recebida de "
            f"{self.titular}: "
            f"+R$ {valor_transferencia:.2f}"
        )

        print("✅ Transferência realizada com sucesso!")

    # MÉTODO PARA MOSTRAR EXTRATO

    def mostrar_extrato(self):

        print(f"""
=========================
EXTRATO DE {self.titular.upper()}
=========================
""")

        # Caso não existam movimentações
        if len(self.extrato) == 0:
            print("⚠️ Nenhuma movimentação realizada.")
            return

        # Exibe todas movimentações
        for movimentacao in self.extrato:
            print(movimentacao)

        print(f"\nSaldo atual: R$ {self.saldo:.2f}")


# CRIAÇÃO DAS CONTAS

# Cria primeira conta
conta1 = ContaBancaria(
    titular="Thiago",
    numero_conta="1001",
    saldo=500
)

# Cria segunda conta
conta2 = ContaBancaria(
    titular="Maria",
    numero_conta="1002",
    saldo=300
)


# TESTES DO SISTEMA

# Realiza depósito
conta1.depositar(200)

# Realiza saque
conta1.sacar(100)

# Realiza transferência
conta1.transferir(150, conta2)

# Mostra saldo das contas
conta1.mostrar_saldo()
conta2.mostrar_saldo()

# Mostra extrato das contas
conta1.mostrar_extrato()
conta2.mostrar_extrato()

