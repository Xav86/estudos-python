numero = 0
soma = 0
contagem = 0
maior = -9999999999
menor = 9999999999

while (numero != -1):
    numero = int(input("Digite um numero: "))
    contagem += 1
    soma = soma + numero

    if numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

soma += 1
media = soma/contagem

print(f"A soma dos numeros deu {soma}, a média {media:.2}. Maior numero {maior} e menor numero {menor}")