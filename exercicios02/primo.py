from random import randint
import math
numero = int(input("Digite um número inteiro: "))

sim = 0
raizNumero = int(math.ceil(math.sqrt(numero)))

if (numero == 1):
    print("Número 1 não é primo >:( ")
elif (numero == 0):
    print("Zero não é primo")
else:
    for i in range(1, raizNumero):
        if(numero % i == 0):
            sim += 1


num_sorteado = randint(1, 100)

if (num_sorteado > 50):
    if (sim == 2) or (numero == 2):
        print(f"Sim, o numero {numero} é primo, parabéns.")
    else:
        print(f"O numero {numero} não é primo.")
else:
    print("Não quero falar >:[ ")

# Forma do professor
# n = int(input("Numero: "))

# i = 1

# div = 0
# #print(f'divisores de {n}')
# while i <= n:
#     if n % i == 0:
#         div += 1
#         #print(i)
#     i += 1
# #print(f"{n} tem {div} divisores")
# if div > 2:
#     print(f'{n} não é primo!')
# else:
#     print(f'{n} é primo!')
