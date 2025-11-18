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