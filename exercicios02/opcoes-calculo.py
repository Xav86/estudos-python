continuar = True
while (continuar):
    n = 0
    n1 = 0
    resultado = 0
    print("------------------------")
    print("Escola uma opção \n Adição (digite 1) \n Subtração (digite 2) \n Multiplicação (digite 3) \n Divisão (digite 4) \n Saida (digite 5)")
    print("------------------------")
    opcao = int(input("Digite a opção: "))
    match opcao:
        case 1:
            n = int(input("Digite um numero: "))
            n1 = int(input("Digite outro numero: "))
            resultado = n + n1
            print(f"\n O resultado da soma é {resultado}")
            continue
        case 2:
            n = int(input("Digite um numero: "))
            n1 = int(input("Digite outro numero: "))
            resultado = n - n1
            print(f"\n O resultado da subtração é {resultado}")
            continue
        case 3:
            n = int(input("Digite um numero: "))
            n1 = int(input("Digite outro numero: "))
            resultado = n * n1
            print(f"\n O resultado da multiplicação é {resultado}")
            continue
        case 4:
            n = int(input("Digite um numero: "))
            n1 = int(input("Digite outro numero: "))
            resultado = n / n1
            print(f"\n O resultado da divisão é {resultado}")
            continue
        case 5:
            continuar = False
        case other:
            print ("não")
