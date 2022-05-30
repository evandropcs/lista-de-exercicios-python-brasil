"""
Exercício 05 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 - A mensagem "Reprovado", se a média for menor do que sete;
 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
Obs: 0 <= nota <= 10

    >>> notas_parciais(10, 4)
    'Aprovado'
    >>> notas_parciais(0, 10)
    'Reprovado'
    >>> notas_parciais(5, 8)
    'Reprovado'
    >>> notas_parciais(10, 10)
    'Aprovado com Distinção'
"""


def notas_parciais(nota_1, nota_2):
    """Escreva aqui em baixo a sua solução"""

    # n1 = float(input('nota 1: '))
    # n2 = float(input('nota 2: '))
    n1 = nota_1
    n2 = nota_2

    media = (n1+n2) / 2

    if media >= 7 and media < 10:
        print("'Aprovado'")
    elif media < 7:
        print("'Reprovado'")
    else:
        print("'Aprovado com Distinção'")