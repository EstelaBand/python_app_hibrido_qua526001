# biblioteca 
import os

# declaração de lista
usuarios = []           # lista é representada por colchetes, aqui vazia pois queremos inserir vários usuários

# Limpa console
os.system("cls")        # aqui a limpeza de tela

while True:
    # menu
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls")            # limpeza de tela
    match opcao:
        case "1":
            usuario = {}         # esse dicionário está vazio pois cada vez q clicar na opção 1 crio um novo dicionário, insiro novo nome
            usuario['nome'] = input("Informe o nome do usuário: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuário: ").strip())
            usuario['email'] = input("Informe o e-mail do usuário: ").strip().lower()
            usuarios.append(usuario)        #  Que é o dicionario, o append ele insere um novo item na lista. 
            os.system("cls")            # limpeza da tela
            print("Novo usuario inserido com sucesso.")
            continue            
        case "2":               #exibir os dados da lista na tela, laço for
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{'-'*40}")
            continue
        case "3":
            break          # aqui ele sai do programa na opção 3           
        case _:
            print("Opção Inválida.")
            continue