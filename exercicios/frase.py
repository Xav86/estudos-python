print("------------Experimentos com string-----------")

frase = input("Digite uma frase: ")
palavra_antiga = input("Digite uma palavra contida na frase acima: ")

print(palavra_antiga in frase) #true ou False

palavra_nova = input("Digite uma nova palavra: ")

print (frase)

frase_nova = frase.replace(palavra_antiga,palavra_nova)

print(frase_nova)