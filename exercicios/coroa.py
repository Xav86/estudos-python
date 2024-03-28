import math

# Solicita os raios ao usuário
raio_maior = float(input("Digite o raio maior da coroa circular: "))
raio_menor = float(input("Digite o raio menor da coroa circular: "))

#calcula
area_coroa = math.pi * (raio_maior**2 - math.pow(raio_menor, 2))
    
# Exibe o resultado
print(f"A área da coroa circular é: {area_coroa:.2f}")