# custo por livro 16,21 / transporte 3reais o prmeiro e 0.75 pro resto

print("---------Custo Capa---------")
desconto = 0.35
preco = 24.95
descontado = preco * desconto
preco = preco - descontado

print (preco)

quant = float(input("Digite o numero de cópias desejada: "))
custo = quant * preco
frete = ((quant-1)*0.75)+3

total = custo + frete

print ("O Valor total da compra ira sair por: ",total)