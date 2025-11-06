# classe
class Pessoa:
    # contrutor  esse é o método que eu crio, o nome do construtor tem quer - dois underlines__ a palavra init e mais dois underlines
    def __init__(self, nome, cpf, email, idade):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Idade: {self.idade} anos")

# algoritimo principal  # instancia a classe #idade recebe zero pq ele é um nome inteiro, tipo de atributo inteiro as aspas duplas para informar que é atributo tipo string
if __name__ == "__main__":
    # instancia a classe    
    usuario = Pessoa(nome="", cpf="", email="", idade=0)  

    # entrada de dados
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.idade = int(input("Informe a idade: ").strip())

    #saida de dados
    usuario.exibir_dados()

    