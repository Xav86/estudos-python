numero = 0
soma = 0

while (numero != -1):
    numero = int(input("Digite um numero: "))
    soma = soma + numero

soma += 1

print(f"A soma dos numeros deu {soma}")