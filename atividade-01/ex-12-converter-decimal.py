print("------------Conversor de decimal-------------")

decimal = int(input("Digite um numero decimal: "))

binario = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(f"o correspondente em hexa, binário e octal de {decimal} são respectivamente {hexadecimal}, {binario} e {octal}")