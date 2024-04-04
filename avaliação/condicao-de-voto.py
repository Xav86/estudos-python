print("------------Condição de voto---------")

idade = float(input("Digite sua idade para sabersua condição de voto: "))

if idade < 16:
    print("Pessoas com menos de 16 anos são proibidas de votar! (proibido)")
elif ((idade >= 16) and (idade < 18) or (idade >= 65)):
    print("Você não é obrigado a votar, porem pode optar caso queira! (optativo)")
elif ((idade >= 18) and (idade < 65)):
    print("Você tem a obrigação de votar! (obrigatório)")
