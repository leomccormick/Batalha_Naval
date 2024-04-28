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
        p = random.choice(LP)
        pais_certo = p == pais_player

    MatrizPlayer = defineBarcos(pais_player)
    MatrizBot = defineBarcosBot(pais_player)
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
        # Pedir Tiro do usuário
        time.sleep(0.5)
        print('Sua vez de atirar!')
        nao_passou = True
        while nao_passou:
            while True:
                tiro = input("Escolha onde será o tiro (LN): ")
                if len(tiro) <2: 
                    print('Digitado errado')
                    time.sleep(0.3)
                else:
                    linha = tiro[1]
                    coluna = tiro[0]
                    if len(tiro) == 3:
                        linha = tiro[1] + tiro[2]
                    if linha in ListaNumeros and coluna in Letras:
                        linha = int(linha)
                        break
                    else:
                        print('Digitado errado')
            time.sleep(0.7)
            if tiros(MatrizBot, linha, coluna) == 'Isso já foi selecionado\nTente novamente':
                nao_passou = True
                print('Isso já foi selecionado\nTente novamente')
            elif tiros(MatrizBot, linha, coluna) == 'Shuaaaaa ... água':
                agua()
                print('Shuaaaaa ... água')
                MatrizBot[linha-1][LpN[coluna]-1] = -2
                MatrizObservada[linha-1][LpN[coluna]-1] = -2
                nao_passou = False
            else:
                boom()
                print('BOOOOOM! Um navio foi acertado')
                MatrizBot[linha-1][LpN[coluna]-1] = -1
                MatrizObservada[linha-1][LpN[coluna]-1] = -1
                nao_passou = False

        mostra_tabuleiros(p, pais_player, MatrizObservada, MatrizPlayer)

        # Ver se Player ganhou - Acao = False
        if foi_derrotado(MatrizBot):
            print('Você ganhou!')
            break

        # Tiro do Bot
        print('Vez do seu oponente atirar!')
        time.sleep(1)
        print('Seu oponente está pensando...')
        time.sleep(1)
        while True:
            linha = random.choice(range(1, 11))
            coluna =  random.choice(Letras)
            if tiros(MatrizPlayer, linha, coluna) == 'Shuaaaaa ... água':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -2
                break
            elif tiros(MatrizPlayer, linha, coluna) == 'BOOOOOM! Um navio foi acertado':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -1
                break

        mostra_tabuleiros(p, pais_player, MatrizObservada, MatrizPlayer)

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