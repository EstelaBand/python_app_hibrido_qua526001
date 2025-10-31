# TODO tarefas

# declaração de dicionário
usuario = {}

# entrada de dados
usuario['nome'] = input("Informe o nome: ").strip().title()
usuario['email'] = input("Informe o e-mail: ").strip().lower()
usuario['telefone'] = input("Informe o telefone: ").strip()
usuario['cpf'] = input("Informe o CPF: ").strip()
usuario['genero'] = input("Informe o genero: ").strip()

# saída de dados
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")



"""
Crie um programa que recebe do usuário os seguintes dados: 
Nome 
E-mail
Telefone
CPF
Gênero
Após isso, o programa deve armazenar esses dados em um dicionário e exibir os dados desse dicionário na tela.
"""

# Entrada de dados