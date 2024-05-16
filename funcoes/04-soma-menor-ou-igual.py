def SomaAnteriores(n):
    """Função que soma os numeros anteriores em relação ao parametro n."""

    i = 0
    soma = 0
    while(n > i):
        soma = soma + i
        i += 1
    return soma

print(SomaAnteriores(4))