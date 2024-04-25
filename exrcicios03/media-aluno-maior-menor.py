notas = []
maior = -999999,2
menor = 9999999,2
i = 0
soma = 0

for i in range(3):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    notas.append(nota)

media = soma/3
print(f"Menor nota: {min(menor)}")
print(f"Maior nota: {max(maior)}")
print(f"média {media:.2}")

notas.sort()
print(notas)
notas.sort(reverse=True)
print(notas)