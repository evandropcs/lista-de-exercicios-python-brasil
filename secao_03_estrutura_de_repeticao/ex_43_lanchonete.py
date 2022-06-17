"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""

    qtd_cachorro = qtd_bauru_s = qtd_bauru_o = qtd_hamburguer = qtd_cheese = qtd_refri  = 0
    preco_cachorro = preco_bauru_s = preco_bauru_o = preco_hamburguer = preco_cheese = preco_refri = 0

    if len(itens) == 0:
        print('_____________________________________________________________________________')
        print('|                              RESUMO DA CONTA                              |')
        print('|---------------------------------------------------------------------------|')
        print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
        print('|---------------------------------------------------------------------------|')
        print(f'| Total Geral:                                    |          0 |       0.00 |')
        print('-----------------------------------------------------------------------------')

    else:

        print('_____________________________________________________________________________')
        print('|                              RESUMO DA CONTA                              |')
        print('|---------------------------------------------------------------------------|')
        print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')

        for cod, qtd in itens:
            if cod == '100':
                qtd_cachorro += qtd
                preco_cachorro = 1.2
            if cod == '101':
                qtd_bauru_s += qtd
                preco_bauru_s = 1.3
            if cod == '102':
                qtd_bauru_o += qtd
                preco_bauru_o = 1.5
            if cod == '103':
                qtd_hamburguer += qtd
                preco_hamburguer = 1.2

            if cod == '104':
                qtd_cheese += qtd
                preco_cheese = 1.3

            if cod == '105':
                qtd_refri += qtd
                preco_refri = 1

        total_qtd = qtd_cachorro + qtd_bauru_s + qtd_bauru_o + qtd_hamburguer + qtd_cheese + qtd_refri
        total_preco = (qtd_cachorro * preco_cachorro) + (qtd_bauru_s * preco_bauru_s) + (qtd_bauru_o * preco_bauru_o) + (qtd_hamburguer * preco_hamburguer) + (qtd_cheese * preco_cheese) + (qtd_refri * preco_refri)

        if qtd_cachorro > 0:
            print(f'| Cachorro Quente  | 100    | 1.20                |          {qtd_cachorro} |{qtd_cachorro * preco_cachorro:11.2f} |')
        if qtd_bauru_s > 0:
            print(f'| Bauru Simples    | 101    | 1.30                |          {qtd_bauru_s} |{qtd_bauru_s * preco_bauru_s:11.2f} |')
        if qtd_bauru_o > 0:
            print(f'| Bauru com Ovo    | 102    | 1.50                |          {qtd_bauru_o} |{qtd_bauru_o * preco_bauru_o:11.2f} |')
        if qtd_hamburguer > 0:
            print(f'| Hamburger        | 103    | 1.20                |          {qtd_hamburguer} |{qtd_hamburguer * preco_hamburguer:11.2f} |')
        if qtd_cheese > 0:
            print(f'| Cheeseburger     | 104    | 1.30                |          {qtd_cheese} |{qtd_cheese * preco_cheese:11.2f} |')
        if qtd_refri > 0:
            print(f'| Refrigerante     | 105    | 1.00                |          {qtd_refri} |{qtd_refri * preco_refri:11.2f} |')

        print('|---------------------------------------------------------------------------|')
        print(f'| Total Geral:                                    |         {total_qtd:2} |{total_preco:11.2f} |')
        print('-----------------------------------------------------------------------------')