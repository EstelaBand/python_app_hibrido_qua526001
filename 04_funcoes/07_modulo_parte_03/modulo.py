# biblioteca
import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# função do 1º grau: a*x + b = 0  
def primeiro_grau(a, b):       # equação de 1º grau calcula a menor distância entre 2 pontos trabalha em 2 dimensões altura e comprimento
    return -b/a if a != 0 else "Não existe raiz real"        # equação de 1º grau a ou b não pdem ser igual a zero
                        
# função do 2º grau : a*x² + b*x + c = 0
def segundo_grau(a, b, c):
    if a != 0:
        delta = (b**2)-(4*a*c)
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)  #math.sqrt é raiz quadrada para calcular
            x2 = (-b - math.sqrt(delta)) / (2*a)
            yield x1
            yield x2        
        elif delta == 0:
            yield -b/(2*a)  # FIXME aqui também vai dar errado o return pois temos que retornar 2 valores então troco pelo yield
        else:
            yield "Não existem raízes reais."  # FIXME 
    else:
        yield primeiro_grau(b,c ) # FIXME esse return aqui vai dar errado mas vamos mudá-lo depois para yield