# importação de bibliotecas
import os

#Loop
while True:
    # limpeza de console
    os.system("cls")

    # tratamento de exceção
    try:
        # entrada de dados
        nome = input("Informe o nome: ").strip().title()
        email = input("Informe o email: ").strip().lower()
        cpf = input("Informe o CPF: ").strip()

        # Limpeza de console
        os.system("cls")

        # saída de dados
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        # menu
        print("1 - Inserir novos dados.")
        print("2 - Sair do programa.")

        opcao = input("Opção desejada: ").strip()

        # verifica a opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
    except:
        print("Não foi possível receber informações.")