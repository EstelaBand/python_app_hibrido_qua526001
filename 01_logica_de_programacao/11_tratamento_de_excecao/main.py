# tratamento de exceção 
try:
    # entrada de dados
    nome = input("Informe o nome :").strip().title()
    idade = int(input("Informe a idade: ").strip())
    altura = float(input("Informe a altura: ").strip().replace(",","."))
    
    # saída de dados
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")

except: 
    print("Infelizmente o programa não pode ser executado.")