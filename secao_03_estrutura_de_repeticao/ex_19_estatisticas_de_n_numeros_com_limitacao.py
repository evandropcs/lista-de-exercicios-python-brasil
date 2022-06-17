"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""

    if len(numeros) ==0:
        print("'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
    else:
        maior = 0
        menor = 99999
        for x in numeros:
            if maior < x:
                maior = x
            if menor > x:
                menor = x
        soma = sum(numeros)
        if menor < 0 or maior > 1000:
            print("'Somente números de 0 a 1000 são permitidos'")
        else:
            print(f"'Maior valor: {maior}. Menor valor: {menor}. Soma: {soma}'")


    # Solução 1:
    # if len(numeros) == 0:
    #     print(f"'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
    # else:
    #     maior = max(numeros)
    #     menor = min(numeros)
    #     soma = sum(numeros)
    #     if menor < 0 or maior > 1000:
    #         print("'Somente números de 0 a 1000 são permitidos'")
    #     else:
    #         print(f"'Maior valor: {maior}. Menor valor: {menor}. Soma: {soma}'")