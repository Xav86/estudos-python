pares = 0

for i in range(0,5):
    numero = int(input("Digite um numero: "))
    if (numero % 2 == 0):
        pares += 1
    
print(f"A quantidade de numeros pares digitados foi de {pares}")