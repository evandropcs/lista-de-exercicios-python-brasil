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

    contar_divisoes = 0
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
                contar_divisoes += 1
    primos = str(primos)
    primos = primos[1:-1]
    divisores = contar_divisoes
    return (primos, divisores)


    # Solução do Roger
#     primos = imprime_apenas_os_primos(n)
#     divisoes = nro_divisoes(n)
#     return (primos, divisoes)
#
#
# def imprime_apenas_os_primos(numero):
#     primos = []
#     for num in range(2, numero + 1):
#         if is_prime(num):
#             primos.append(str(num))
#
#     return ", ".join(primos)
#
#
# def is_prime(numero):
#     """retorna se o número é primo
#     """
#     prime = True
#     for num in range(2, numero):
#         resto_divisao = numero % num
#         if resto_divisao == 0:
#             prime = False
#             break
#     return prime
#
#
# def divisoes(numero):
#     """retorna se o número é primo"""
#     divisoes = 0
#     for num in range(2, numero):
#         divisoes += 1
#
#     return divisoes







