print("-----------Validação de data---------")

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

#alumas verificações do dia
if (dia == 0):
    validacao_dia = "Invalido"
    motivo_dia = "Não existe dia 0"
elif (dia < 0):
    validacao_dia = "Invalido"
    motivo_dia = "Não existe dia negativo"
elif (dia > 31):
    validacao_dia = "Invalido"
    motivo_dia = "Não existe mês com mais de 31 dias"
else:
    validacao_dia = "Valido"
    motivo_dia = "" 

#alumas verificações do mês
if (mes == 0):
    validacao_mes = "Invalido"
    motivo_mes = "Não existe mes 0"
elif (mes < 0):
    validacao_mes = "Invalido"
    motivo_mes = "Não existe mes negativo"
elif (mes > 12):
    validacao_mes = "Invalido"
    motivo_mes = "Não existe mais de 12 meses"
else:
    validacao_mes = "Valido"
    motivo_mes = ""

#alguma verificações do ano
if (ano == 0):
    validacao_ano = "Invalido"
    motivo_ano = "Não existe ano 0"
elif (ano < 0):
    validacao_ano = "Invalido"
    motivo_ano = "Não existe ano negativo"
elif (ano > 2024):
    validacao_ano = "Invalido"
    motivo_ano = "Não existe ano maior que 2024, ainda"
else:
    validacao_ano = "Valido"
    motivo_ano = ""

#reportando situação para o usuário
if ((validacao_dia == "Valido") and (validacao_mes  == "Valido") and (validacao_ano  == "Valido")):
    print (f"{dia}/{mes}/{ano} é uma data valida")

elif ((validacao_dia == "Invalido") and (validacao_mes  == "Valido") and (validacao_ano  == "Valido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_dia}")

elif ((validacao_dia == "Valido") and (validacao_mes  == "Invalido") and (validacao_ano  == "Valido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_mes}")

elif ((validacao_dia == "Valido") and (validacao_mes  == "Valido") and (validacao_ano  == "Invalido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_ano}")

elif ((validacao_dia == "Invalido") and (validacao_mes  == "Invalido") and (validacao_ano  == "Valido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_dia} e {motivo_mes}")

elif ((validacao_dia == "Invalido") and (validacao_mes  == "Valido") and (validacao_ano  == "Invalido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_dia} e {motivo_ano}")

elif ((validacao_dia == "Valido") and (validacao_mes  == "Invalido") and (validacao_ano  == "Invalido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_mes} e {motivo_ano}")

elif ((validacao_dia == "Invalido") and (validacao_mes  == "Invalido") and (validacao_ano  == "Invalido")):
    print(f"{dia}/{mes}/{ano} é uma data invalida, pois: {motivo_dia} , {motivo_mes} e {motivo_ano}")

else:
    print("Erro! Favor contratar um programador melhor!")