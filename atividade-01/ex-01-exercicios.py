print ("-------------exercicio 01---------------")

numero1 = float(input("Digite um numero qualquer: "))

dobro = numero1*2

print (f"O dobro deste numero é {dobro}")

comprimento = float(input("Digite o comprimento que tem a sala: "))
largura = float(input("Digite a largura que tem a sala: "))

area = comprimento * largura

print (f"A area desta sala é de {area} metros quadrados")

valor = float(input("Digite o valor do produto: "))
desconto = 0.5

valor_descontado = valor-(valor*0.5)

print (f"O produto recebeu 50% de desconto, indo de {valor} para {valor_descontado}")