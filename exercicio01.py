print("Bem-vindo a loja do Ramon Leopoldo")
valor_pedido = int(input("Entre o valor do pedido R$"))
quantidade_parcela = int(input("Entre a quantidade de parcelas:"))

if (quantidade_parcela<4):
    #Parcela menor que 4 juro de  0%
    valor_parcela = valor_pedido/quantidade_parcela #calculando valor da parcela
    print(f'valor da parcela R${valor_parcela:.2f} \nValor total parcelado R${valor_pedido:.2f}')
elif (quantidade_parcela>= 4 and quantidade_parcela<6):
    #elif maior igual 4 e menor que 6 deve ser atribuido 4% de juros.
    valor_parcela = ((4/100)+1)*valor_pedido/quantidade_parcela #calculando valor da parcela com o juros
    valor_total_pedido = valor_parcela*quantidade_parcela #calculo valor total ja com o juros
    print(f'valor da parcela R${valor_parcela:.2f} \nValor total parcelado R${valor_total_pedido:.2f}')
elif (quantidade_parcela>= 6 and quantidade_parcela<9):
    #Parcelas maior ou igual a 6 e menor que 9 deve ser atribuido 8% de juros.
    valor_parcela = ((8/100)+1)*valor_pedido/quantidade_parcela #calculando valor da parcela com o juros
    valor_total_pedido = valor_parcela*quantidade_parcela #calculo valor total ja com o juros
    print(f'valor da parcela R${valor_parcela:.2f} \nValor total parcelado R${valor_total_pedido:.2f}')
elif (quantidade_parcela>= 9 and quantidade_parcela<13):
    #parcelas maior ou igual a 9 e menor que 13 deve ser atribuido 16% de juros
    valor_parcela = ((16/100)+1)*valor_pedido/quantidade_parcela #calculando valor da parcela com o juros
    valor_total_pedido = valor_parcela*quantidade_parcela #calculo valor total ja com o juros
    print(f'valor da parcela R${valor_parcela:.2f} \nValor total parcelado R${valor_total_pedido:.2f}')
else :
    # parcelas igual ou maior que 13 devem ser atribuido 32% de juros.
    valor_parcela = ((32/100)+1)*valor_pedido/quantidade_parcela #calculando valor da parcela
    valor_total_pedido = valor_parcela*quantidade_parcela #calculo valor total ja com o juros
    print(f'valor da parcela R${valor_parcela:.2f} \nValor total parcelado R${valor_total_pedido:.2f}')