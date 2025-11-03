# biblioteca
import os
import math

# limpa console
def limpar():           # ao invés de digitar sempre os.system vou digitar limpar
    os.system("cls")

# funções de cálculo    # área do quadrado ladox2
def quadrado(l):
    return l**2

def retangulo(b, h):    # aqui tenho dois paramentros, base e altura, então coloco vírgula para separar
    return b*h

def triangulo(b, h):
    return (b*h)/2      # base x altura dividido por 2

def hipotenusa(c1, c2):
    return math.sqrt((c1**2) + (c2**2))

# TODO: Atividade: Crie uma nova função para calcular a hipotenusa do triângulo-retângulo
# NOTE: para calcular raiz quadrada, importe a biblioteca "math" e use a função "math.sqrt()".


# algoritmo principal
limpar()

while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular Hipotenusa")
    print("5 - Sair do Programa")
    opcao = input("Opção desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            resultado = quadrado(l)   #onde l é lado
            limpar()
            print(f"Área do quadrado: {resultado}")
            continue            
        case "2":
            b = float(input("Informe a base do retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do retângulo: ").strip().replace(",","."))
            resultado = retangulo(b, h)
            limpar()
            print(f"Área do retângulo: {resultado}")
            continue
        case "3":
            b = float(input("Informa a base do triângulo: ").strip().replace(",","."))
            h = float(input("Informa a altura do triângulo: ").strip().replace(",","."))
            resultado = triangulo(b, h)
            print(f"Área do triângulo: {resultado}")
            continue
        case "4": 
            c1 = float(input("Digite o comprimento do primeiro cateto: ").strip().replace(",","."))
            c2 = float(input("Digite o comprimento do segundo cateto: ").strip().replace(",","."))
            resultado = hipotenusa(c1, c2)
            limpar()
            print(f"A hipotenusa é: {resultado}")
            continue        
        case "5":
            break
        case _:
            print("Opção inválida")
            continue

