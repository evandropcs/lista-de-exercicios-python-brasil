"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""

    contdiv = 0
    numeros = list(range(3, n + 1))
    primos = list()
    if n > 1:
        primos = [2]
        for num in numeros:
            cont = 0
            for valor in range(1, num + 1):
                if num % valor == 0:
                    cont += 1
            if cont == 2:
                primos.append(num)
                contdiv += 1
    primos = str(primos)
    primos = primos[1:-1]
    divisores = contdiv
    return (primos, divisores)







