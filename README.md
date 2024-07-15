<h1>Atividades de logica de programação e algoritimos</h1>
<h2>QUESTÃO 1 de 4</h2>
<p>Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que aceita cartões de crédito. Uma das estratégias de vendas dessa empresa X é cobrar um Juros maior conforme a quantidade de parcelas que o cliente desejar, conforme a listagem abaixo:</p>
<ul> 
  <li>Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);</li>
  <li>Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);</li>
  <li>Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);</li>
  <li>Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);</li>
  <li>Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);</li>
</ul>
<p>O valor da parcela é calculado da seguinte maneira:
valorDaParcela= (valorDoPedido*(1+juros))/quantidadeParcelas</p>
<p>O valor total parcelado é calculado da seguinte maneira:
valorTotalParcelado=valorDaParcela*quantidadeParcelas </p>
<h2>Requisitos</h2>
<ol>
  <li>Elabore um programa em Python que:
  Deve-se implementar o <code>print</code> com o seu nome completo (somente print, não usar input aqui).[EXIGÊNCIA DE CÓDIGO 1 de 6]
    <ol>
      <li>Por exemplo: <code>print(“Bem-vindos a loja do Bruno Kostiuk”)</code></li>
    </ol>
  
  </li>
  <li>Deve-se implementar o <code>input</code> do <code>valorDoPedido</code> e da <code>quantidadeParcelas</code> [EXIGÊNCIA DE CÓDIGO 2 de 6];</li>
  <li>Deve-se implementar o Juros conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];</li>
  <li>Deve-se implementar o <code>valorDaParcela</code> e <code>valorTotalParcelado</code> [EXIGÊNCIA DE CÓDIGO 4 de 6];</li>
  <li>Deve-se implementar as estruturas <code>if</code>, <code>elif</code> e <code>else</code> (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6]; </li>
  <li>Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];</li>
</ol>
<h3>QUESTÃO 2 de 4</h3>
<p>Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Marmitas de Bife Acebolado ou Filé de Frango. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto. <br> A Loja possui seguinte relação: </p>
<ul>
<li>Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;</li>
<li>Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;</li>
<li>Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;</li>
</ul>
<h3>Requisitos</h3>
<p>Elabore um programa em Python que:</p>
<ol>
  <li>Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
    <ol>
      <li>Por exemplo: <code>print(“Bem vindos a loja de Marmitas do Bruno Kostiuk”)</code>. Além do seu nome completo, deve-se implementar um <code>print</code> com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];
      </li>
    </ol>
  </li>
  <li>Deve-se implementar o <code>input</code> do sabor (BA/FF) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de BA e FF [EXIGÊNCIA DE CÓDIGO 2 de 8];</li>
  <li>Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];</li>
  <li>Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];</li>
  <li>Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];</li>
  <li>Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];</li>
  <li>Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];</li>
  <li>Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];</li>
  <li>Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];</li>
  <li>Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];</li>
</ol>
<h2> QUESTÃO 3 de 4</h2>
 <p >Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma fábrica que vende Camisetas em atacado. Você ficou com a parte de desenvolver a interface com o funcionário. <br> A Fábrica opera as vendas da seguinte maneira:</p>
  <p>Modelos e valores</p>
  <ul>
    <li> Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos;</li>
    <li>Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos; </li>
    <li> Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos;</li>
    <li> Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos;</li>
  </ul>
  <p>Descontos</p>
  <ol>
    <li>Se número de camisetas for menor que 20 não há desconto na venda;</li>
    <li>Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%;</li>
    <li>Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%;</li>
    <li>Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%;</li>
    <li>Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas;</li>
  </ol>
  <p>Adicionais frete</p>
  <ul>
    <li>Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais;</li>
    <li>Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais;</li>
    <li>Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais;</li>
  </ul>
<p>O valor final da conta é calculado da seguinte maneira: <br>
total = (modelo \* num_camisetas) + frete

<h2>Requisitos</h2>
<p>Elabore um programa em Python que:</p>
<ol> 
  <li>Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
  Por exemplo: print(“Bem vindos a Fábrica de Camisetas do Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 7];</li>
  <li>Deve-se implementar a função escolha_modelo() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];</li>
    <ol> 
      <li>Pergunta o modelo desejado;</li>
      <li>Retorna o valor do modelo com base na escolha do usuário (use return);</li>
      <li>Repete a pergunta do item 2 se digitar uma opção diferente de: MCS/MLS/MCE/MLE;</li>
    </ol>
  <li>Deve-se implementar a função <code>num_camisetas()</code> em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
    <ol>
      <li>Pergunta o número de camisetas;</li>
      <li>Retorna (use return) o número de camisetas com desconto seguindo a regra do enunciado (desconto calculado em cima do número de camisetas);</li>
      <li>Repete a pergunta do item 2.1 se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)</li>
    </ol>
  </li>
  <li>Deve-se implementar a função frete() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7]; </li>
      <ol>
        <li> Pergunta pelo serviço adicional de frete;</li>
        <li> Retorna (use return) o valor de apenas uma das opções de frete </li>
        <li> Repetir a pergunta item 2.1 se digitar uma opção diferente de: 1/2/0;</li>
      </ol>
  <li>Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];</li>
  <li>Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7]</li>
  <li>G.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];</li>
</ol>

<h1>QUESTÃO 4 de 4</h1>
<h2>Enunciado</h2>
<p>
  Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de funcionários. Este software deve ter o seguinte menu e opções:
</p>
<ol>
  <li>Cadastrar Funcionário</li>
  <li>Consultar Funcionário
    <ol>
      <li>Consultar Todos</li>
      <li>Consultar por Id</li>
      <li>Consultar por setor</li>
      <li>Retornar ao menu</li>
    </ol>
  </li>
  <li>Remover Funcionário</li>
  <li>Encerrar Programa</li>
</ol>

<h2>Elabore um programa em Python que:</h2>
<ol>
  <li>
    Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
    <ul>
      <li>Por exemplo: <code>print(“Bem vindos a empresa do Bruno Kostiuk”)</code> [EXIGÊNCIA DE CÓDIGO 1 de 8]</li>
    </ul>
  </li>
  <li>
    Deve-se implementar uma lista com o nome de <code>lista_funcionarios</code> e a variável <code>id_global</code> com valor inicial igual ao número de seu RU [EXIGÊNCIA DE CÓDIGO 2 de 8];
  </li>
  <li>
    Deve-se implementar uma função chamada <code>cadastrar_funcionario(id)</code> em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
    <ol>
      <li>Pergunta nome, setor, salario do funcionário;</li>
      <li>Armazena o id (este é fornecido via parâmetro da função), nome, setor, salario dentro de um dicionário;</li>
      <li>Copiar o dicionário para dentro da <code>lista_funcionarios</code> (utilizar o <code>copy</code>);</li>
    </ol>
  </li>
  <li>
    Deve-se implementar uma função chamada <code>consultar_funcionarios()</code> em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
    <ol>
      <li>Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu):
        <ul>
          <li>Se Consultar Todos, apresentar todos os funcionários com todos os seus dados cadastrados;</li>
          <li>Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o funcionário específico com todos os seus dados cadastrados;</li>
          <li>Se Consultar por Setor, solicitar ao usuário que informe o setor, e apresentar o(s) funcionário(s) do setor com todos os seus dados cadastrados;</li>
          <li>Se Retornar ao menu, deve-se retornar ao menu principal (<code>return</code>);</li>
          <li>Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta 4.1.</li>
          <li>Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir.</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>
  Deve-se implementar uma função chamada <code>remover_funcionario()</code> em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
    <ol>
      <li>Deve-se pergunta pelo id do funcionário a ser removido;</li>
      <li>Remover o funcionário da <code>lista_funcionarios</code>;</li>
      <li>Se o id fornecido não for de um funcionário da lista, printar “Id inválido” e repetir a pergunta 5.1</li>
    </ol>
  </li>
  <li>
    Deve-se implementar uma estrutura de menu no código principal (<code>main</code>), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
    <ol>
      <li>Deve-se pergunta qual opção deseja (1. Cadastrar Funcionário / 2. Consultar Funcionário / 3. Remover Funcionário / 4. Encerrar Programa):
        <ul>
          <li>Se Cadastrar Funcionário, incrementar em um <code>id_global</code> e chamar a função <code>cadastrar_funcionario(id_global)</code>;</li>
          <li>Se Consultar Funcionário, chamar função <code>consultar_funcionario()</code>;</li>
          <li>Se Remover Funcionário, chamar função <code>remover_funcionario()</code>;</li>
          <li>Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);</li>
          <li>Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta 6.1</li>
          <li>Enquanto o usuário não escolher a opção 4, o menu deve se repetir.</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>
    Deve-se implementar uma lista de dicionários (uma lista contendo dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
  </li>
  <li>
    Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
  </li>
</ol>
