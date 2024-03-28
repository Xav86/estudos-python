print("---------Média Aluno (classico)--------")

nome = input("Digite seu nome: ")

n1 = float(input("Digite a primira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

soma = (n1 + n2 + n3)/3

if soma >= 7.00 :
    resultado = "aprovado"
else :
    resultado = "reprovado"

print ("O aluno",nome," foi", resultado," com à média de:",soma)