print("-----------calculo de salario mensal-----------")

salario_por_hora = float(input("Digite o quanto você ganha por hora de trabalho: "))
horas_trabalhadas_mes = float(input("Digite o quanto você trabalha por mês, em horas: "))

#salario bruto
salario_bruto = salario_por_hora * horas_trabalhadas_mes

#Imposto de renda
ir = salario_bruto*0.11

#INSS
inss = salario_bruto*0.08

#sindicato
sindicato = salario_bruto*0.05

#salario liquido
salario_liquido = ((salario_bruto - ir)-inss)-sindicato

print("Seu salario bruto é de: ",salario_bruto,"\n Seu salario liquido é de: ",salario_liquido,"\n Sendo que  foi pago",ir," no Imposto de renda",inss," do INSS e mais ",sindicato," para o sindicato")