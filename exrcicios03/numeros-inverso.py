i = 0
numeros = []

for i in range(10):
    numero = float(input("Digite um numero: "))
    numeros.append(numero)

numeros.sort(reverse=True)
print(numeros)