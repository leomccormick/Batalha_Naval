from constantes import *
from operacoes import *

game = True
while game:
    # definir pais do player
    while True:
        pais_player = input('Qual país você quer ser? (Japão, Rússia, Austrália, França, Brasil): ')
        if pais_player in LP:
            break
        else:
            print('País Indisponível')
    pais_certo = True
    while pais_certo:
        pais_bot = random.choice(LP)
        pais_certo = pais_bot == pais_player

    MatrizPlayer = defineBarcos(pais_player)
    MatrizBot = defineBarcosBot(pais_bot)
    # Para testes:
    # print(MatrizBot)
    MatrizObservada = [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
    
    while True:
        # Pedir tiro do usuário
        time.sleep(0.5)
        print('Sua vez de atirar!')
        while True:
            while True:
                tiro_player = input("Escolha onde será o tiro (LN): ")
                if len(tiro_player) <2: 
                    print('Digitado errado')
                    time.sleep(0.3)
                else:
                    linha = tiro_player[1]
                    coluna = tiro_player[0]
                    if len(tiro_player) == 3:
                        linha = tiro_player[1] + tiro_player[2]
                    if linha in ListaNumeros and coluna in Letras:
                        linha = int(linha)
                        break
                    else:
                        print('Digitado errado')
            time.sleep(0.7)
            print(MatrizBot)
            print()
            if tiro(MatrizBot, linha, coluna) == 'Isso já foi selecionado\nTente novamente':
                print('Isso já foi selecionado\nTente novamente')
            elif tiro(MatrizBot, linha, coluna) == 'Shuaaaaa ... água':
                print('Shuaaaaa ... água')
                MatrizBot[linha-1][LpN[coluna]-1] = -2
                MatrizObservada[linha-1][LpN[coluna]-1] = -2
                break
            else:
                print('BOOOOOM! Um navio foi acertado')
                tipo_barco = MatrizBot[linha-1][LpN[coluna]-1]
                MatrizBot[linha-1][LpN[coluna]-1] = -1
                MatrizObservada[linha-1][LpN[coluna]-1] = -1
                if not barcoRestante(MatrizBot, tipo_barco):
                    print('Você afundou um {0}!'.format(n_barco[int(str(tipo_barco)[0])]))
                    time.sleep(2)
                break
                        

        mostra_tabuleiros(pais_bot, pais_player, MatrizObservada, MatrizPlayer)

        # Ver se Player ganhou - Acao = False
        if foi_derrotado(MatrizBot):
            print('Você ganhou!')
            break

        # tiro do Bot
        print('Vez do seu oponente atirar!')
        time.sleep(1)
        print('Seu oponente está pensando...')
        time.sleep(1)
        while True:
            linha = random.choice(range(1, 11))
            coluna =  random.choice(Letras)
            if tiro(MatrizPlayer, linha, coluna) == 'Shuaaaaa ... água':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -2
                break
            elif tiro(MatrizPlayer, linha, coluna) == 'BOOOOOM! Um navio foi acertado':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -1
                break

        mostra_tabuleiros(pais_bot, pais_player, MatrizObservada, MatrizPlayer)

        # Ver se Bot ganhou - Acao = False
        if foi_derrotado(MatrizPlayer):
            print('Você perdeu...')
            break

    while True:
        x = input('Jogar novamente? (Sim ou Não): ')
        if x == 'Sim':
            break
        elif x == 'Não':
            game = False
            print('Obrigado por jogar!\nDesenvolvido por Felipe Carbonell e Leonardo Veras :)')
            break
        else:
            print('Digitado errado')