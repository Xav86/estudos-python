print("-----------Troca de valores--------------")

numero1 = float(input("Digite um valor: "))
numero2 = float(input("Digite outro valor: "))

print (f"O primeiro valor é {numero1} e o segundo valor {numero2}")

numero2, numero1 = numero1, numero2

print (f"Agora o primeiro valor é {numero1} e o segundo valor é {numero2}")