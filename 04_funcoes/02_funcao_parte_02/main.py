# biblioteca
import os


# função
def boas_vindas(nome):
    os.system("cls")   # esse limpa depois, após o usuário digitar o nome ele vai limpar o campo informe seu nome
    print(f"Seja bem vindo, {nome} 👱‍♀️ ")


# algoritmo principal
os.system("cls")        #esse executa primeiro, limpa os campos para chamar o nome 
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)