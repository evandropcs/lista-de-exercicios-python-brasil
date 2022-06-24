"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    n = numero

    cen, n = divmod(n, 100)
    dez, und = divmod(n, 10)

    str_und = 'unidade'; str_unds = 'unidades'; str_dez = 'dezena'; str_dezs = 'dezenas';
    str_cen = 'centena'; str_cens = 'centenas'

    if numero >= 1000:
        print("'O número precisa ser menor que 1000'")
    elif numero < 0:
        print("'O número precisa ser positivo'")
    elif cen > 1 and dez > 1 and und > 1:
        print(f"'{numero} = {cen} {str_cens}, {dez} {str_dezs} e {und} {str_unds}'")
    elif cen > 1 and dez > 1 and und == 0:
        print(f"'{numero} = {cen} {str_cens} e {dez} {str_dezs}'")
    elif cen > 1 and dez == 1 and und == 0:
        print(f"'{numero} = {cen} {str_cens} e {dez} {str_dez}'")
    elif cen > 1 and dez == 1 and und == 1:
        print(f"'{numero} = {cen} {str_cens}, {dez} {str_dez} e {und} {str_und}'")
    elif cen == 1 and dez == 1 and und == 1:
        print(f"'{numero} = {cen} {str_cen}, {dez} {str_dez} e {und} {str_und}'")
    elif cen == 1 and dez == 0 and und == 1:
        print(f"'{numero} = {cen} {str_cen} e {und} {str_und}'")
    elif cen > 1 and dez == 1 and und > 1:
        print(f"'{numero} = {cen}{str_cens}{dez}{str_dez}{und}{str_unds}'")
    elif cen > 1 and dez == 0 and und == 0:
        print(f"'{numero} = {cen} {str_cens}'")
    elif cen == 1 and dez == 0 and und == 0:
        print(f"'{numero} = {cen} {str_cen}'")
    elif cen > 1 and dez == 0 and und > 1:
        print(f"'{numero} = {cen} {str_cens} e {und} {str_unds}'")
    elif cen > 1 and dez == 0 and und == 1:
        print(f"'{numero} = {cen} {str_cens} e {und} {str_und}'")
    elif cen == 0 and dez > 1 and und > 1:
        print(f"'{numero} = {dez} {str_dezs} e {und} {str_unds}'")
    elif cen == 0 and dez > 1 and und == 1:
        print(f"'{numero} = {dez} {str_dezs} e {und} {str_und}'")
    elif cen == 0 and dez > 1 and und == 0:
        print(f"'{numero} = {dez} {str_dezs}'")
    elif cen == 0 and dez == 1 and und == 0:
        print(f"'{numero} = {dez} {str_dez}'")
    elif cen == 0 and dez == 1 and und > 1:
        print(f"'{numero} = {dez} {str_dez} e {und} {str_unds}'")
    elif cen == 0 and dez == 0 and und > 1:
        print(f"'{numero} = {und} {str_unds}'")
    elif cen == 0 and dez == 0 and und == 1:
        print(f"'{numero} = {und} {str_und}'")


