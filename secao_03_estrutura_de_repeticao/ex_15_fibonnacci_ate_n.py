"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.

    >>> calcular_serie_de_fibonacci(1)
    '1'
    >>> calcular_serie_de_fibonacci(2)
    '1, 1'
    >>> calcular_serie_de_fibonacci(3)
    '1, 1, 2'
    >>> calcular_serie_de_fibonacci(4)
    '1, 1, 2, 3'
    >>> calcular_serie_de_fibonacci(5)
    '1, 1, 2, 3, 5'
    >>> calcular_serie_de_fibonacci(6)
    '1, 1, 2, 3, 5, 8'
    >>> calcular_serie_de_fibonacci(7)
    '1, 1, 2, 3, 5, 8, 13'

"""


def calcular_serie_de_fibonacci(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    primeiro = 1
    ultimo = 1
    lista = 1
    if n != 1:
        n -= 1
        print(f"'{lista}", end=", ")

        for x in range(n):
            if x == n-1:
                print(f"{lista}'")
            else:
                print(f"{lista}", end=", ")
                lista = primeiro + ultimo
                primeiro = ultimo
                ultimo = lista
    else:
        print(f"'{lista}'")




