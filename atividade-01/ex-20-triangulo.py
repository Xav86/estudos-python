print("---------Calculando triangulo----------")
#lado1+lado2 > lado3

lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
    
if lado1 == lado2 == lado3:
    print("Os valores inseridos podem formar um triangulo equilátero!")

else:
    if ((lado1 + lado2) >= lado3):        
        if (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
            print("Os valores inseridos podem formar um triangulo isósceles!")

        elif (lado1 != lado2) or (lado2 != lado3) or (lado1 != lado3):
            print("Os valores inseridos podem formar um triangulo escaleno!")

    else:
        print("isso não é um trianulo... :(")