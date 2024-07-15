print("---------Bem vindo a empresa de Ramon Leopoldo---------")
print("-------------------------------------------------------")
listas_funcionario = []
id_global = 0
#Deve-se implementar uma função chamada cadastrar_funcionario(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
def cadastrar_funcionario(id):
    print("---------------MENU CADASTRO FUNCIONARIO---------------")
    nome = input("Digite o nome do funcionario: ")
    setor = input("Digite o setor do funcionario: ")
    salario = input("Digite o salario do funcionario: ")
    funcionario = {
        "id" : id,
        "nome" : nome,
        "setor" : setor,
        "salario" : salario
    }
    listas_funcionario.append(funcionario)
    print("Funcionario cadastrado com sucesso.")
#Deve-se implementar uma função chamada consultar_funcionarios() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
def consultar_funcionarios():
    while True:
      print("--------------MENU CONSULTAR FUNCIONARIO---------------")
      print("Digite a opção deseja\n[1] Consultar todos\n[2] Consultar por id\n[3] Consultar por setor\n[4] Retornar ao menu")
      opcao = input(">>")
      #Se Consultar Todos, apresentar todos os funcionários com todos os seus dados cadastrados;
      if opcao == "1":
        for funcionario in listas_funcionario:
          print(f"ID: {funcionario['id']}, Nome: {funcionario["nome"]}, Setor: {funcionario["setor"]}, Salario: {funcionario["salario"]}")
      #Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o funcionário específico com todos os seus dados cadastrados;
      elif opcao == "2":
        id_encontrado = False
        id_informado = int(input("Digite o id que deseja verificar"))
        for funcionario in listas_funcionario:
          if funcionario["id"] == id_informado:
            print("USUARIO POR ID ENCONTRADO.")
            print(f"ID: {funcionario["id"]}\n Nome: {funcionario["nome"]}\n Setor: {funcionario["setor"]}\n Salario: {funcionario["salario"]}")
            id_encontrado = True
        if id_encontrado == False:
          print("ID nao encontrada, digite uma id valida.")
      #Se Consultar por Setor, solicitar ao usuário que informe o setor, e apresentar o(s) funcionário(s) do setor com    todos os seus dados cadastrados;
      elif opcao == "3":
        setor_encontrado = False
        setor_informado = input("Digite o setor que deseja verificar: ")
        for funcionario in listas_funcionario:
          if funcionario["setor"] == setor_informado:
            print(f"ID: {funcionario["id"]}\n Nome: {funcionario["nome"]}\n Setor: {funcionario["setor"]}\n Salario: {funcionario["salario"]}")
            setor_encontrado = True
        if setor_encontrado == False:
          print("Não encontramos nem um funcionario no setor informado.")
      #Se Retornar ao menu, deve-se retornar ao menu principal (return);
      elif opcao == "4":
        return
      #Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
      else:
        print("Opção desejada invalida.")
#Deve-se implementar uma função chamada remover_funcionario() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
def remover_funcionario():
  while True:
    id_encontrado = False
    print("---------------MENU REMOÇÃO FUNCIONARIO----------------")
    id_remover = int(input("Digite o ID que deseja remover: "))
    for funcionario in listas_funcionario:
      if funcionario["id"]== id_remover:
        listas_funcionario.remove(funcionario)
        print("Funcionario removido.")
        id_encontrado=True
        break
    if id_encontrado == False:
      print("ID nao encontrada.")
#Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
while True:
  print("---------------------MENU INICIAL----------------------")
  print("1. Cadastrar Funcionário \n2. Consultar Funcionário \n3. Remover Funcionário \n4. Encerrar Programa)")
  opcao_desejada = input(">>")
  if opcao_desejada == "1":
    id_global+=1
    cadastrar_funcionario(id_global)
  elif opcao_desejada == "2":
    consultar_funcionarios();
  elif opcao_desejada == "3":
    remover_funcionario()
  elif opcao_desejada == "4":
    print("Encerrando programa...")
    break
  else:
    print("Opção invalida.")

        
            

    
  