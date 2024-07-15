
def escolha_modelo():
    print()
    modelo = input("Entre com o modelo desejado\n"
                   "Camiseta Manga Curta Simples (MCS)\n" 
                   "Camiseta Manga Longa Simples (MLS)\n" 
                   "Camiseta Manga Curta Com Estampa (MCE)\n" 
                   "Camiseta Manga Longa Com Estampa (MLE)\n"
                    ">>")
    #Verificando as condições de entrada do usuario, a condição que entrar vai retornar o valor unitario da camisa.
    if modelo == "MCS":
        return 1.80
    elif modelo == "MLS": 
        return 2.10
    elif modelo == "MCE" :
        return 2.90
    elif modelo=="MLE":
        return 3.20
    else:
        #Caso nao entre em nem uma condição acima vai cair no else informando escolha invalida e puxando a função novamente com as informações para o usuario digitar
        print("Escolha invalida entre com modelo novamente")
        return escolha_modelo()
def num_camisas () :
    while True:
        try:
            numero_camisetas = input("Digite o numero de camisas: \n >>")
            numero_camisetas = int(numero_camisetas)
            #As condições virificam a quantidade digitada pelo usuario atribuindo o valor de desconto a depender do numero de camisas, o desconto é dado em cima da quantidade de camisas.
            if numero_camisetas<20 :
                #sem desconto
                return numero_camisetas
            elif numero_camisetas>=20 and numero_camisetas < 200 :
                #Desconto de 5%
                valor_numero_camiseta = numero_camisetas-((numero_camisetas*5)/100)
                return valor_numero_camiseta
            elif numero_camisetas >= 200 and numero_camisetas < 2000:
                #Desconto de 7%
                valor_numero_camiseta = numero_camisetas-((numero_camisetas*7)/100)
                return valor_numero_camiseta
            elif numero_camisetas >=200 and numero_camisetas <=20000 :
                #Desconto de 12%
                valor_numero_camiseta = numero_camisetas-((numero_camisetas*12)/100)
                return valor_numero_camiseta
            else: #Caso o valor seja maior que 20.000 vai cair no else e chamando novamente a função
                print("Não aceitamos pedidos nessa quantidade de camisetas.")
        #except com informaçoes de que o valor digitado esta invalido, caso o usuario digite algo que nao seja numeros e de problemas na hora da conversão
        except :
            print("Digite um valor valido")
def frete():
    while True:
        #Essa função pede para o usuario digitar o valor de frete desejado.
        opcao_frete = input("Escolha a opção de frete:\n"
                            "[1] Frete por transportadora R$ 100.00\n"
                            "[2] Frete por Sedex R$ 200.00\n" 
                            "[0] Retirar o pedido na fabrica R$ 0.00\n"
                            ">>")
        #Condições para verificar a opção desejada entre as opções 0, 1 ou 2
        if opcao_frete == "0":
            valor_frete = 0
            return valor_frete
        elif opcao_frete== "1":
            valor_frete = 100
            return valor_frete
        elif opcao_frete == "2":
            valor_frete = 200
            return valor_frete
        else : 
        # Se caso nao for digitada opção diferente de 0,1 ou 2 cai neste else e infroma opção invalida e retorna a função novamente pedindo para digitar novamente.
            print("Opção de frete invalida")
print("Bem vindo a fabrica de camisetas de Ramon Leopoldo")
modelo = escolha_modelo()
camisa = num_camisas()
opcao_frete = frete()
total= (modelo*camisa)+opcao_frete
print (f'Valor total a ser pago {total:.2f}')