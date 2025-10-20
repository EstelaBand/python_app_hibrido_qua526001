# declaração de variáveis
nome = input("Informe seu nome: ").strip().title() 
idade = int(input("Informe sua idade: ").strip())
altura = float(input("Informe sua altura: ").strip().replace(",","."))

# saída de dados
print(f"Nome de usuário: {nome}. Tipo: {type(nome)}")
print(f"idade: {idade}. Tipo: {type(idade)}")
print(f"Altura: {altura} metros. Tipo: {type(altura)}")
            