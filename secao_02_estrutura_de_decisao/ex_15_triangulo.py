"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >>> classificar_triangulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_triangulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_triangulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_triangulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_triangulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_triangulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_triangulo(lado_a: float, lado_b: float, lado_c: float):
    """Escreva aqui em baixo a sua solução"""

    l_a = lado_a
    l_b = lado_b
    l_c = lado_c

    if (l_a + l_b) < l_c or (l_a + l_c) < l_b or (l_b+ l_c) < l_a:

        print("'Não é um triângulo'")

    else:
        if l_a == l_b and l_a == l_c:
            print("'Triângulo Equilátero'")
        elif l_a == l_b or l_a == l_c:
            print("'Triângulo Isósceles'")
        else:
            print("'Triângulo Escaleno'")