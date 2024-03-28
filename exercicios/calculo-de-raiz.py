import math

x1 = input("Digite o valor de x1: ")
x2 = input("Digite o valor de x2: ")
y1 = input("Digite o valor de y1: ")
y2 = input("Digite o valor de y2: ")

distancia = math.sqr(((x2-x1)**2)+((y2-y1)**2))

print(f"O distancia enre os dois pontos é {distancia}")