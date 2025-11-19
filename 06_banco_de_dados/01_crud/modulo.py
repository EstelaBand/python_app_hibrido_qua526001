import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o gênero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()

        # filtra atributo email das pessoas que possuem mesmo e-mail informado
        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado."
        else:
            nova_pessoa = Pessoa(
                nome=nome,
                nascimento=nascimento,
                email=email,
                genero=genero
            )

            #insert into pessoa esse é o insert do banco de dado, o session.add
            session.add(nova_pessoa)
            session.commit()

            return f"Pessoa {nova_pessoa.nome} cadastrada com sucesso."
            
    except Exception as e:
        print(f"Não foi possível cadastrar. {e}.")



# read
def listar (session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()  #pega todos os dados do banco para listar na tela

        print("Pessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Gênero: {pessoa.genero}")
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
            print(f"\n{'-'*40}\n")


    except Exception as e:
         print(f"Não foi possível listar. {e}.")

# update
def atualizar(session, Pessoa):
    id_pessoa = "" # eu coloco somente aspas pois estou só inicializando
    email = ""
    novo_nome = ""
    novo_email = ""
    novo_nascimento = ""
    novo_genero = ""

    try:
        print("Escolha o campo que deseja pesquisar: ")
        print("1 - ID")
        print("2- E-mail")
        print("3 - Retornar")
        opcao = input("Opção desejada: ").strip()
        limpar()

        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa).first()
            case "2":
                email = input("Informe o e-mail: ").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                return "Opção inválida."

        # aqui, no if pessoa, vou dar opção de qual dado ele vai alterar então precisamos mostrar o objeto com seus atributos
        if pessoa:
            while True:  # lastro de repetição
                print(f"ID {pessoa.id_pessoa}")
                print("Qual campo deseja alterar:\n")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - Gênero: {pessoa.genero}")
                print(f"5 - Finalizar")
                campo = input("Campo desejado: ").strip()
                limpar()  
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if email in [pessoa.email for pessoa in pessoas]:
                            print("E-mail já cadastrado.")
                        continue                
                    case "3":
                        novo_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip() #esses campos(novo nascimento, novo nome, novo genero etc) são nomeados de acordo com o update, lá em cima o update já deu esses nomes para os campos, devem ser iguais
                        continue
                    case "4":
                        novo_genero = input("Informe o novo gênero: ").strip().lower()
                        continue
                    case "5": #no case 5 caso eu não renomeie um campo ele vai manter o nome antigo, ou data antiga é a confirmação dos dados para confirmar o que o usuário mudou
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        novo_nascimento = datetime.strptime(novo_nascimento,"%d/%m/%Y").date() if novo_nascimento != "" else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                        break
                    case _:
                        print("Campo inexistente.")
                        continue
            pessoa.nome = novo_nome # agora que realmente vai atualizar
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero

            session.commit() #para atualizar os dados, depois return

            return "Dados atualizados com sucesso."
        else: #se eu não encontrar a pessoa vem agora o else
            return "Pessoa não encontrada."
    except Exception as e:
        print(f"Não foi possível alterar os dados. {e}.")
    