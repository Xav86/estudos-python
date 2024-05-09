d = ()
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
endereco = input("Digite o seu endereço: ")
telefone = int(input("Digite a idade: "))

d = { 'nome':nome, 'idade':idade, 'endereço': endereco, 'telefone': telefone}

print(dict(d))