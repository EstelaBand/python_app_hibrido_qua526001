# biblioteca
import os      # essa trabalha com a limpeza de dados

# classe  # criar uma pessoa na classe, para dar um nome para uma classe, toda classe obrigatoriamente tem que começar com letra Maiuscula sempre. Se uma classe possuir um nome composto ele não será separado por underscore_ a primeira letra de cada palavra será maiuscula e tudo junto. ex; EstelaBandeira, CaixaVerde
class Pessoa:
    #atributos      esses são os atributos
    nome = "Estela Bandeira"
    idade = 12
    email = "estela@gmail.com"

    # método   aqui podemos nomear e utilizar underscore_ Se o método não recebe parâmetro, diferente da função, ele precisa ter algo entre os parênteses mesmo que em tese não exista dados, a palavra self, padrão da linguagem python, toda vez que criei metodo sem parametro, DIGITO self dentro dos parênteses, e se ele receber algo vou digitar self "a vírgula ," e o parametro ex. self, "parametro"
    def exibir_dados(self): # o método é exibir dados, a ação, ou função para ser executada necessita da função, ela é isolada.
        print(f"Nome: {self.nome}")         
        print(f"Idade: {self.idade}")
        print(f"Nome: {self.email}")

if __name__ == "__main__": #no if name o if tem espaço e ele está fora da classe, observe, foda da identação
    # instancia a classe (cria novo objeto)
    usuario = Pessoa() # isso é uma instãncia, essa pessoa tem nome, idade e email dentro do meu programa, agora quero exibir os dados dessa pessoa, para exibir os dados eu vou chamar o meu objeto, o self é só dentro da classe agora ao chamar o parenteses pode ficar vazio

    # limpa console
    os.system("cls" if os.name == "nt" else "clear")  # para limpar a tela

    # saída de dados
    usuario.exibir_dados()

    