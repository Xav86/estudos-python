print ("----------Imposto de Renda (simplificado)------------")

remuneracao = float(input("Digite sua renda mensal: "))
#dedução atual = 25% da primeira faixa
deducao = 564.80
valor_base = remuneracao - deducao

if (valor_base < 2259.20):
    total = valor_base

elif ((valor_base > 2259.20) and (valor_base <= 2826.65)):
    total = (valor_base*0.075) - 169.44

elif ((valor_base > 2826.65) and (valor_base <= 3751.05)):
    total = (valor_base*0.15) - 381.44

elif ((valor_base > 3751.05) and (valor_base <= 4664.68)):
    total = (valor_base*0.2250) - 662.77

elif ((valor_base > 4664.68) and (valor_base <= 99999.99)):
    total = (valor_base*0.2750) - 896.00

print (f"O total qual tera que pagar de Imposo de Renda simplificado sera de: {total:,.2f}")