print("--------------maior e menor numero-------------")

numero1 = float(input("Digite o valor do primeiro numero: "))
numero2 = float(input("Digite o valor do segundo numero: "))
numero3 = float(input("Digite o valor do terceiro numero: "))

if (numero1 == numero2) and (numero2 == numero3):
    print("Todos os numeros são iguais!")

elif (numero1 > numero2) and (numero1 > numero3):
    maior = numero1
elif (numero2 > numero3) and (numero2 > numero1):
    maior = numero2
elif (numero3 > numero2) and (numero3 > numero1):
    maior = numero3

if (numero1 < numero2) and (numero1 < numero3):
    menor = numero1
elif (numero2 < numero3) and (numero2 < numero1):
    menor = numero2
elif (numero3 < numero2) and (numero3 < numero1):
    menor = numero3

print("Maior numero é,", maior, ". e o menor, ",menor)