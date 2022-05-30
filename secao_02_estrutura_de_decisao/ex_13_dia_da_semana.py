"""
Exercício 13 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

    >>> calcular_dia_da_semana(1)
    'Domingo'
    >>> calcular_dia_da_semana(2)
    'Segunda'
    >>> calcular_dia_da_semana(3)
    'Terça'
    >>> calcular_dia_da_semana(4)
    'Quarta'
    >>> calcular_dia_da_semana(5)
    'Quinta'
    >>> calcular_dia_da_semana(6)
    'Sexta'
    >>> calcular_dia_da_semana(7)
    'Sábado'
    >>> calcular_dia_da_semana(8)
    'Dia Inválido'
    >>> calcular_dia_da_semana(0)
    'Dia Inválido'

"""


def calcular_dia_da_semana(numero: int):
    """Escreva aqui em baixo a sua solução"""

    n = numero

    if n == 1:
        print("'Domingo'")
    elif n == 2:
        print("'Segunda'")
    elif n == 3:
        print("'Terça'")
    elif n == 4:
        print("'Quarta'")
    elif n == 5:
        print("'Quinta'")
    elif n == 6:
        print("'Sexta'")
    elif n == 7:
        print("'Sábado'")
    else:
        print("'Dia Inválido'")