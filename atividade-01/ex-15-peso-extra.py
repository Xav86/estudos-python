print("----------rendimento diário----------")

peso = int(input("Digite o peso do peixe em Kg: "))

if peso <= 50:
    print("Peixes menor que o estabelecido pelo regulamento de pesca do Estado (50 quilos). Sendo assim não é necessario pagar nada. :)")
else:
    excesso = peso - 50
    multa = excesso * 4
    print ("Peixe maior que o estabelecido pelo regulamento de pesca do Estado (50 quilos) deve pagar uma multa de R$",multa)