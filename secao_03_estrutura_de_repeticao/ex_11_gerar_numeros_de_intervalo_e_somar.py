"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao


Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido.
Também mostre a soma dos números da sequência.

    >>> calcular_numeros_no_intervalo_e_somar(1, 10)
    'Sequência: 1, 2, 3, 4, 5, 6, 7, 8, 9. Soma: 45'
    >>> calcular_numeros_no_intervalo_e_somar(-10, -1)
    'Sequência: -10, -9, -8, -7, -6, -5, -4, -3, -2. Soma: -54'
    >>> calcular_numeros_no_intervalo_e_somar(-1, -10)
    'Sequência: vazia. Soma: 0'

"""


def calcular_numeros_no_intervalo_e_somar(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    if set(range(inicio, fim)) == set([]):
        print("'Sequência: vazia. Soma: 0'")
    else:
        soma = 0

        print("'Sequência: ", end='')

        for x in range(inicio, fim):
            soma += x
            if x == (fim - 1):
                print(f"{x}", end='')
            else:
                print(f"{x}", end=', ')

        print(f". Soma: {soma}'", end='')

    # Solução 1:

    # numeros = str(list(range(inicio, fim)))
    # numeros = numeros[1: -1]
    # soma = sum((list(range(inicio, fim))))
    # if set(numeros) != set([]):
    #     print(f"'Sequência: {numeros}. Soma: {soma}'")
    # else:
    #     print(f"'Sequência: vazia. Soma: {0}'")
