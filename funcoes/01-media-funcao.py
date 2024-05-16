"""Teste funções"""

def media(s, n):
    """Função Media"""
    if n != 0:
        return s/n
    else:
        return None


def main():
    """Função principal"""
    contador = 0
    soma = 0

    while contador < 4:
        num = int(input('Digite um numero: '))
        soma = soma + num
        contador = contador + 1

    print(f'Media é {media(soma, contador)}')


if __name__ == '__main__':
    main()