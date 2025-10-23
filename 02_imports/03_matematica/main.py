# biblioteca
import math

# entrada de dados
r = float(input("Informe o raio do círculo: ").strip().replace(",","."))

# cálculos
a = math.pi*(r**2)
c = 2*math.pi*r

# saída de dados
print(f"Número do pi: {math.pi}")
print(f"Área da circunfência: {a:.2f}")
print(f"Tamanho da circunferência: {c:.2f}")