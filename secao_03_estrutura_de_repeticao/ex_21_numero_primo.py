"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(9)
    False
    >>> eh_primo(10)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(547)
    True
    >>> eh_primo(548)
    False

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""

    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        lista = []
        for x in range(2, n+1):
            if n % x == 0:
                lista.append(x)
        if len(lista) == 1:
            return True
        else:
            return False





    # x = 1
    # lista = []
    #
    # if n < 2:
    #     print("False")
    # else:
    #     while x <= n:
    #         if n % x == 0 and x != 1 and x != n:
    #             lista.append(x)
    #             x += 1
    #         else:
    #             x += 1
    #
    #     if len(lista) == 0:
    #         print("True")
    #     else:
    #         print("False")

    # resultado = 0
    # x = 1
    #
    # if n == 0:
    #     print("False")
    # elif n == 2:
    #     print("True")
    # else:
    #     while x <= n:
    #        if n % x != 0:
    #            x += 1
    #        else:
    #            resultado += 1
    #            x += 1
    #
    #     if resultado == 2:
    #         print("True")
    #     else:
    #         print("False")







