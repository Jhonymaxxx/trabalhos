#     Trabalho Jhony Max de Souza RU: 4462553
def dimensoesObjeto():  # início função dimensoesObjeto()
    while True:  # laço de repetição enquanto verdadeiro
        try:      # verificação de erro de digitação
            altura = int(input('| Digite a altura do volume em (cm):  '))   # pede a 1° medida do volume
            comprimento = int(input('| Digite o comprimento do volume em (cm):  '))  # pede a 2° medida do volume
            largura = int(input('| Digite a largura do volume em (cm):  '))  # pede a 3° medida do volume
            volume = int(altura * comprimento * largura)  # calcula a cubagem do volume
            v = volume
            print('| O volume possui em (cm³): {}'.format(v))  # mostra o resultado da cubagem
            if (v <= 1000):    # verifica o volume para retornar o valor
                return 10.00
            elif (1000 <= volume < 10000):  # verifica o volume para retornar o valor
                return 20.00
            elif (10000 <= volume < 30000):   # verifica o volume para retornar o valor
                return 30.00
            elif (30000 <= volume < 100000):   # verifica o volume para retornar o valor
                return 50.00
            else:
                print('| Dimensões passaram do limite \n| digite as dimensões desejadas novamente') # verifica se o tamanho do volume é transportavél
            continue # volta ao início do laço
        except ValueError:  # soluciona problema em caso de valores não númericos
            print(
                '| Você digitou valor não numérico \n| digite as dimensões desejadas novamente')  # mostra o erro e orienta a digitar novamente
            continue

# final função dimensoesObjeto()
def pesoObjeto():   # início função pesoObjeto()
    while True: # laço de repetição enquanto verdadeiro
        try:  # verificação de erro de digitação
            peso = float(input('| Digite o peso do volume em (kg): '))  # solicita a digitação do peso do volume
            p = peso
            if (p <= 0.1):  # verifica o peso para retornar o valor
                return 1
            elif (0.1 <= peso < 1):  # verifica o peso para retornar o valor
                return 1.5
            elif (1 <= peso < 10):   # verifica o peso para retornar o valor
                return 2
            elif (10 <= peso < 30):   # verifica o peso para retornar o valor
                return 3
            else:
                print('| Não aceitamos volumes tão pesados')  # verifica se o peso está dentro do padrão aceito
            continue  # volta ao incio do laço
        except ValueError:  # soluciona problema em caso de valores não númericos
            print('| Você digitou valor não numérico \n| Por favor entre com o peso desejado novamente')
            continue

## final função pesoObjeto()
def rotaObjeto():    # início função rotaObjeto()
    while True:  # laço de repetição enquanto verdadeiro
        try:  # verificação de erro de digitação
            rota = (input(
                '              Rotas         \n| RS - De Rio de Janeiro  \  São Paulo:  \n| BS - De Brasília  \  São Paulo: \n| RB - De Rio de Janeiro  \  Brasília: \n| Selecione a rota:  '))  # pede o destino do envio
            rota = rota.upper()  # resolve problema letra minúscula
            r = rota
            if (r == 'RS'):  # calcula a rota e retorna o valor
                return 1

            elif (r == 'BS'):   # calcula a rota e retorna o valor
                return 1.2

            elif (r == 'RB'):    # calcula a rota e retorna o valor
                return 1.5
            else:
                print('| Você digitou uma rota que não existe')   # checa se a rota é atendida
            continue   # volta ao incio do laço
        except ValueError:   # soluciona problema em caso de valores não númericos
            print('| Você digitou uma rota que não existe Por favor entre com a rota desejada novamente')
            continue

# final função rotaObjeto()

# início Main
print('_______________________________________________________________________')
print('|       RU: 4462553 JHONY MAX DE SOUZA TRANSPORTES E LOGÍSTICA        |')
print('|                                                                     |')
v = dimensoesObjeto()  # retorna o valor da função
p = pesoObjeto()    # retorna o valor da função
r = rotaObjeto()   # retorna o valor da função
print('| Total a pagar R$:{:.2f} (volume: {} * Peso: {} * Rota: {})'.format(v * p * r, v, p, r))  # mostra o valor total do frete e a composição do preço

