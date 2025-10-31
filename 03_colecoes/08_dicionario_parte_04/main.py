# declaração de coleções
usuarios = [
    {
        'nome': "Fulano",
        'idade': 20,
        'email':"fulano@gmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email':"cicrano@gmail.com"    
    },
    {
        'nome': "Beltrano",
        'idade': 30,
        'email':"beltrano@gmail.com"
    }  
]

# exibindo os dados dos usuários
for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")


"""
for linha in tabela:
    for coluna in linha:
        dado da célula
"""