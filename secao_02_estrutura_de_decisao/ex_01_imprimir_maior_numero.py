"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça dois números e imprima o maior deles.

    >>> maior_de_dois_numeros(2,3)
    3
    >>> maior_de_dois_numeros(-1,-10)
    -1
    >>> maior_de_dois_numeros(-5,3)
    3
    >>> maior_de_dois_numeros(7,-14)
    7
"""


def maior_de_dois_numeros(x, y):
    """Escreva aqui em baixo a sua solução"""

    # n1 = int(input('Numero 1'))
    # n2 = int(input('Numero 2'))

    # n1=int([0])
    # n2=int([1])

    n1 = x
    n2 = y
    if n1 > n2:
        print(n1)
    else:
        print(n2)