print ("----------Calculo de Juros Compostos----------")

pv = float(input("Digite um valor para investimento inicial: "))
i = float(input("Digite a valor aplicado mensalmente (taxa): "))
m = float(input("Digite o numero de meses: "))

fv = pv * ((1+i/100/12)**m)

print(f'O montante sera de: {fv:.2f}')