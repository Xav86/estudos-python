lista = []
i=0
for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("========== ORDEM DE ENTRADA ===========")
i = 0
for i in range(5):
    print(f"{lista[i]} - {i}")

print("========== ORDEM REVERSA ===========")

tam = len(lista)
i = tam -1
while i != 0-1:
    print(f"{lista[i]} - {i}")
    i -= 1