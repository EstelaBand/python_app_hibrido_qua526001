# classes  # nesse programa a classe pessoa é pai e as classe pessoa fisica e juridica são filhos e estão herdando email e telefone
class Pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):  # quando eu criei esse método ele já passou para a pessoa fis e juri sem eu precisar fazer mais nada
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

class PessoaFisica(Pessoa): # A classe Pessoa é uma super classe e a classe PessoaFisica é uma subclasse. Quem herda é sub classe, é filho. E quem passa é o pai. Generalização ou Herança. 
    def __init__(self, nome, cpf, idade, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email=email, telefone=telefone) # eu não preciso colocar acima na função def self email e self telefone pois ele vai herdar da class Pessoa esses dados. Então o comando super vai fazer herdar email telefone 

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, telefone=telefone)
            
    def exibir_dados(self):
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()