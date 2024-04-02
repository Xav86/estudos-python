print("---------------Área do circulo-----------------")

raio = float(input("Digite um número de unidade de comprimento"))
pi = 3.14159

area = pi*(raio**2)

if (raio <= 0):
    print("Erro: valores negativos não são permitidos.")
else:
    print(f"A área do círculo de raio {raio:.2} unidades e {area:.2} unidades.")