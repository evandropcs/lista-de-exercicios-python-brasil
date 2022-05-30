"""
Exercício 06 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    5
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    -1
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    3
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    15
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""

    # n1 = int(input('Numero 1'))
    # n2 = int(input('Numero 2'))
    # n3 = int(input('Numero 3'))

    n1 = x
    n2 = y
    n3 = z

    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)
