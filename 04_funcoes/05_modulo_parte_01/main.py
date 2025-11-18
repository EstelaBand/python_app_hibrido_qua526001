# importa as funções
import modulo as m

m.limpar()
while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular Círculo")
    print("5 - Calcular Trapézio")
    print("6 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    m.limpar()
    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            m.limpar()
            area = m.quadrado(l)
            print(f"Área do quadrado {area}")
            continue
        case "2":
            b = float(input("Informe a base do retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do retângulo: ").strip().replace(",","."))
            m.limpar()
            area = m.retangulo(b, h)
            print(f"Área do retângulo: {area}")
            continue
        case "3":
            b = float(input("Informe a base do triângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do triângulo: ").strip().replace(",","."))
            m.limpar()
            area = m.triangulo(b, h)
            print(f"Área do triângulo {area}")
            continue
        case "4":
            r = float(input("Informe o raio do círculo: ").strip().replace(",","."))
            m.limpar()
            area = m.circulo(r)
            print(f"Área do círculo {area}")
            continue
        case "5":
            b = float(input("Informe a base menor do trapézio: ").strip().replace(",","."))
            B = float(input("Informe a base maior do trapézio: ").strip().replace(",","."))
            h = float(input("Informe a altura do trapézio: ").strip().replace(",","."))
            m.limpar()
            area = m.trapezio(b, B, h)
            print(f"Área do trapézio: {area}")
            continue
        case "6":
            break
        case _:
            print("Opção inválida.")
            continue