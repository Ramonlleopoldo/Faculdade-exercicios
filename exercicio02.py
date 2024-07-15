
valor = 0.0
condicao = True
print("-----Bem vindo a loja de marmitas de Ramon Leopoldo-----")
print("------------------------Cardapio------------------------")
print("--------------------------------------------------------")
print("---|Tamanho|Bife acebolado (BA) | File de frango (FF)---")
print("---|   P   |        R$16        |           R$15     ---")
print("---|   M   |        R$18        |           R$17     ---")
print("---|   G   |        R$22        |           R$21     ---")
print("--------------------------------------------------------")

while True:
    tamanhoInvalido = False
    sabor = ""
    tamanho = ""
    sabor = input("Entre com sabor desejado (BA) ou (FF): ")
    #condicional para saber se o sabor é bife acebolado
    if sabor=="BA":
        #condicional para verificar o tamanho
        tamanho = input("Digite o tamanho [P] [M] [G] : ")
        if tamanho == 'P':
            valor += 16
            print("Você pediu um bife acebolado tamanho [P] no valor de R$16 \n")
        else:
            if tamanho== 'M':
                valor +=18
                print("Você pediu um bife acebolado tamanho [M] no valor de R$18 \n")
            else:
                if tamanho == 'G':
                    valor += 22
                    print("Você pediu um bife acebolado tamanho [G] no valor de R$22 \n")
                else:
                    #se caso o tamanho nao for nem uma das opçoes aceitaiveis [P][M] ou [G] o tamanho ivanlido vai receber true
                    tamanhoInvalido = True
                    print("Tamanho invalido, tente novamente. \n")
        #se o tamanho invalido for true vai cair no if retornando ao começo do programa
        if (tamanhoInvalido):
            continue
        else:
        #se o tamanho invalido for false vai cair no else perguntando se deseja algo a mais
            opcao = input("gostaria de pedir algo mais? (S/N) ")
            if opcao == 'N' or opcao=='n':
                break
            elif opcao == 'S' or opcao == "s":
                continue
    #Condicional para saber se o sabor é frango frito
    elif sabor=="FF":
        #Condicionais para verificar o tamanho
        tamanho = input("Digite o tamanho [P] [M] [G] : ")
        if tamanho == 'P':
            valor += 15
            print("Você pediu um filé de frango tamanho [P] no valor de R$15\n")
        else:
            if tamanho== 'M':
                valor +=17
                print("Você pediu um filé de frango tamanho [M] no valor de R$17\n")
            else:
                if tamanho == 'G':
                    valor += 21
                    print("Você pediu um filé de frango tamanho [G] no valor de R$21\n")
                else:
                   #se caso o tamanho nao for nem uma das opçoes aceitaiveis [P][M] ou [G] o tamanho ivanlido vai receber true
                   tamanhoInvalido = True 
                   print("Tamanho invalido, tente novamente. \n")
        #se o tamanho invalido for true vai cair no if retornando ao começo do programa
        if (tamanhoInvalido):
            continue
        else:
             #se o tamanho invalido for false vai cair no else perguntando se deseja algo a mais
            opcao = input("gostaria de pedir algo mais? (S/N) ")
            if opcao == 'N' or opcao=='n':
                break 
            elif opcao == 'S' or opcao == "s":
                continue
    #Caso o sabor nao seja FF ou BF vai cir no else informando o sabor invalido
    else :
        print("Sabor invalido, tente novamente. \n")
#print final apos o while encerrar informando o valor final
print(f'Valor total a ser pago é R${valor}')
    

