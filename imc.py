print ("----------Calculo do IMC------------")

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

if imc < 16:
    condicao = "baixo peso (grau |)"
elif imc >= 16 and imc < 17:
    condicao = "baixo peso (grau ||)"
elif imc >= 17 and imc < 18.50:
    condicao = "baixo peso (grau |||)"
elif imc >= 18.50 and imc < 25:
    condicao = "Peso ideal, parabéns! :D"
elif imc >= 25 and imc < 30:
    condicao = "Você está com sobrepeso, um pouco mais que deveria"
elif imc >= 30 and imc < 35:
    condicao = "Obesidade (grau |)"
elif imc >= 35 and imc < 30:
    condicao = "Obesidade (grau ||, severa)"
elif imc >= 40:
    condicao = "Obesidade (grau |||, morbida) :()"

print("Seu Imc é",imc,", nesta condição você está com",condicao)

