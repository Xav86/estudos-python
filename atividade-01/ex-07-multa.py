print("--------------calculo multa-----------")

velocidade_permitida = int(input("Digite a velocidade maxima permitida em uma avenida: "))
velocidade_motorista = int(input("Digite a velocidade que você estava dirigindo: "))

velocidade_extra = velocidade_motorista - velocidade_permitida 

if (velocidade_motorista <= velocidade_permitida):
    print("Você estava dentro da velocidade permitida, portanto não recebera multa.")
elif (velocidade_extra <= 10):
    print(f"Você passou {velocidade_extra}Km/h acima da velocidade maxima permitida de {velocidade_permitida}. Devera pagar uma multa de R$ 85,13 e levara uma multa Leve, com 3 pontos na carteira.")
elif ((velocidade_extra > 10) or (velocidade_extra <= 30)):
    print(f"Você passou {velocidade_extra}Km/h acima da velocidade maxima permitida de {velocidade_permitida}. Devera pagar uma multa de R$ 127,69 e levara uma multa Média, com 5 pontos na carteira.")
elif (velocidade_extra > 31):
    print(f"Você passou {velocidade_extra}Km/h acima da velocidade maxima permitida de {velocidade_permitida}. Devera pagar uma multa de R$ 574,62 e levara uma multa Gravissima, com 7 pontos na carteira.")
else:
    print("Erro X( ")