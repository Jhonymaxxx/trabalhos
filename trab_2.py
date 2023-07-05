#                 Trabalho 2 Jhony Max de Souza RU: 4462553
print('|----------------------------CARDÁPIO-------------------------------|')  #  ínicia mostrando o cardápio na tela
print('|          Seja Bem vindo! à Lanchonete Jhony Max de Souza          |')
print('|__CÓDIGO_|__________________DESCRIÇÃO__________________|VALOR(R$)__|')
print('| 100     | Cachorro-Quente                             |R$:  9,00  |')
print('| 101     | Cachorro-Quente Duplo                       |R$: 11,00  |')
print('| 102     | X-Egg                                       |R$: 12,00  |')
print('| 103     | X-Salada                                    |R$: 13,00  |')
print('| 104     | X-Bacon                                     |R$: 14,00  |')
print('| 105     | X-Tudo                                      |R$: 17,00  |')
print('| 200     | Refrigerante Lata                           |R$:  5,00  |')
print('| 201     | Chá Gelado                                  |R$:  4,00  |')
total = 0  # acumula o valor dos pedidos
while 'true':  # laço de repetição
    cod = int(input('Didigite o código do pedido escolhido: '))   #   solícita a escolha através do código
    if cod!=100 and cod!=101 and cod!=102 and cod!=103 and cod!=104 and cod!=105 and cod!=200 and cod!=201:  # confirma se o código existe no cardápio
        print('Código inválido! ')   #  imprime caso o código seja inválido
        continue  # volta ao começo do laço
    if cod == 100:
        print('Você escolheu Cachorro-Quente R$: 9,00 ')  # mostra a ecolha referente ao código
        total = total + 9  # soma os valores
    elif cod == 101:
        print('Você escolheu Cachorro-Quente Duplo R$: 11,00')    # mostra a ecolha referente ao código
        total = total + 11  # soma os valores
    elif cod == 102:
        print('Você escolheu X-Egg R$: 12,00 ')       # mostra a ecolha referente ao código
        total = total + 12  # soma os valores
    elif cod == 103:
        print('Você escolheu X-Salada R$: 13,00 ')     # mostra a ecolha referente ao código
        total = total + 13  # soma os valores
    elif cod == 104:
        print('Você escolheu X-Bacon R$: 14,00 ')      # mostra a ecolha referente ao código
        total = total + 14  # soma os valores
    elif cod == 105:
        print('Você escolheu X-Tudo R$: 17,00 ')     # mostra a ecolha referente ao código
        total = total + 17  # soma os valores
    elif cod == 200:
        print('Você escolheu Refrigerante Lata R$: 5,00 ')      # mostra a ecolha referente ao código
        total = total + 5  # soma os valores
    elif cod == 201:
        print('Você escolheu Chá Gelado R$: 4,00 ')      # mostra a ecolha referente ao código
        total = total + 4  # soma os valores

    fechar = input('Deseja pedir mais alguma coisa? \n1 - sim...\n0 - não...\n>>>')  # pergunta se haverá novos pedidos e orienta o cliete na escolha
    fechar = fechar.upper()  # resolução problrma s / S
    if fechar == '1':  # caso digite S volta ao ínicio para nova escolha
        print('próximo pedido')
        continue  # leva ao ínicio do laço
    else: #  caso não queira mais nada e precione enter
        print('O valor total a pagar é R$: {:.2f}'.format(total))   # imprime o valor total a ser pago
        print('Obigado pela preferência volte sempre')  #  agradeçe ao cliente
        break  # encerra o programa
