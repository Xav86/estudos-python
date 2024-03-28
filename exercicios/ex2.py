print("=====Dividindo números======")
a = float(input("digite um numero:"))
b = float(input("digite outro numero:"))

try:
    print ("Resultado da divisão: ",a/b)
except ZeroDivisionError:
    print ("Divisão por zero - invalida!")