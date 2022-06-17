"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""

    if len(data) < 2:
        return 'Data inválida'
    else:

        dia, mes, ano = data.split('/')
        dia, mes, ano = int(dia), int(mes), int(ano)
        erro = 0

        if dia < 0 or dia > 31:
            erro += 1

        if mes < 1 or mes > 12:
            erro += 1

        if mes == 2 and dia > 28:
            erro += 1

        if erro > 0:
            return 'Data inválida'
        else:
            return 'Data válida'

    # if len(data) < 7:
    #     print("'Data inválida'")
    # elif data[1] and data[3] or data[2] and data[5] == "/":
    #     if int(data[0]) >= 3 and int(data[4]) == 2:
    #         print("'Data inválida'")
    #     elif data[2] == "/" and int(data[4]) >= 3:
    #         print("'Data inválida'")
    #     else:
    #         print("'Data válida'")

