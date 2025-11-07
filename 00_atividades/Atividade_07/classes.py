# classes
class ContaPessoal:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def exibir_dados(self):
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.conta}")
        print(f"Saldo: {self.saldo}")

class TitularConta(ContaPessoal):
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.nome = nome
        self.cpf = cpf
        super().__init__(agencia = agencia, conta = conta, saldo = saldo)

    def exibir_dados(self):
        return super().exibir_dados()