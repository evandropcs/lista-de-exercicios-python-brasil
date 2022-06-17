"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1
    >>> calcular_media(1, 3)
    2
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""


def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""

    soma = 0
    elementos = 0

    if notas == ():
        print("'É necessária ao menos uma nota para calcular a média'")
    elif notas != 0:
        for x in notas:
            soma += x
            elementos += 1

        media = soma / elementos
        media = media * 1.0
        if media % 1 == 0.0:
            print(f"{media:.0f}")
        else:
            print(media)



