#               trabalho Jhony Max de Souza RU: 4462553
print('+-------------------------------------------------------------+')
print('|          Bem vindo ao atacadão do Jhony Max de Souza        |')  #  ínicio do programa
print('+-------------------------------------------------------------+')
print('|     Calcule seu desconto, sobre a quantidade de itens       |')  # mostra o propósito programa
print('+-------------------------------------------------------------+')

valor_produto = float(input('|Digite aqui o valor unitário do produto desejado: '))   # variável que pede o valor do produto a ser calculado
qtd_produto = int(input('|Digite a Quantidade desejada: '))  # variável que pede a quantidade para saber o valor do desconto
desconto_produto = 0    # variável que acumula os produtos


if qtd_produto <= 9:                                  # outra maneira. if qtd_produto < 10               checa a quantidade para aplicar o desconto
  desconto_produto = 0.00
elif qtd_produto >= 10 and qtd_produto < 100:         # outra maneira. elif  qtd_produto > 9 and qtd_produto <= 99:       checa a quantidade para aplicar o desconto
  desconto_produto = 0.05
elif qtd_produto >= 100 and qtd_produto < 1000:       #  outra maneira. elif qtd_produto > 99 and qtd_produto <= 999:         checa a quantidade para aplicar o desconto
  desconto_produto = 0.10
else:
  desconto_produto = 0.15                            # apartir de 1000 unidades 0.15% de desconto

total_sem_desconto = qtd_produto * valor_produto   # calcula o valor sem desconto
print('|O valor total sem desconto é de: R$ {:.2f}'.format(total_sem_desconto))    # mostra o valor total sem desconto

total_com_desconto = total_sem_desconto - total_sem_desconto  * desconto_produto    # calcula o valor com o desconto
print('|Valor total com desconto é de: R$ {:.2f}  (desconto:{:.2f} %)  |'.format(total_com_desconto,desconto_produto))   # mostra o valor com o desconto aplicado
print('|_____________________________________________________________|')
print('|                  Agradecemos a preferência                  |')    # após o calculo agradece ao cliente
print('|                        Volte Sempre!                        |')
print('|_____________________________________________________________|')
#                               fim do programa