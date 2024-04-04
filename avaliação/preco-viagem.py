print ("--------Preço da viagem--------")

distancia = float(input("Digite qual sera a distancia percorrida em Km: "))

if (distancia > 200):
    preco = distancia * 0.45
else:
    preco = distancia * 0.50

print(f"O valor que dever ser pago para percorrer {distancia}Km, sera de {preco}.") 