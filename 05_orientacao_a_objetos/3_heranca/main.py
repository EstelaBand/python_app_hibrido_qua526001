# biblioteca do Python  #deixo um espaço entre a biblioteca do python e a que criamos dentro de classes
import os

# nossa biblioteca
from classes import PessoaFisica, PessoaJuridica

# funçao limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear") # o cls limpa tela no windows eu chamo nt se for linux clear.

# função principal
def main():
    usuario = PessoaFisica(nome="", cpf="", idade=0, email="", telefone="")  # eu posso identar a instancia do objeto para não ficar tão comprido. eu identaria como vou fazê-lo na próxima linha da empresa. Abaixo está identado e não escrito em linha reta.
    empresa = PessoaJuridica(
        nome_fantasia="",
        cnpj="",
        email="",
        telefone=""
    )

    limpar()
    while True #o menu o usuário vai poder inserir dados da pessoa, dados da empresa, exibir todos os dados e sair do programa
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados da empresa")
        print("3 - Exibir dados do usuário")
        print("4 - Exibir dados da empresa")
        print("5 - Sair do programa")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                usuario.nome = input("Informe seu nome: ").strip().title()
                usuario.cpf = input("Informe seu CPF: ").strip()
                usuario.idade =int(input("Informe sua idade: ").strip())
                usuario.email = input("Informe seu email: ").strip().lower()
                usuario.telefone = input("Informe seu telefone: ").strip()
                limpar()
                continue
            case "2":
                empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
                empresa.cnpj = input("Informe o CNPJ: ").strip()
                empresa.email = input("Informe o email da empresa: ").strip().lower()
                empresa.telefone = input("Informe o telefone da empresa: ").strip()
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

if __name__ == "__main__":
    main()