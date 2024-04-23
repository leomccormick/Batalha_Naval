import random, time

# Valores e cores do mapa
# Vazio = Preto = 0
# Barco existente = Verde = 1
# Barco atingido = Vermelho = -1
# Água atingida = Azul = -2

def mostra_tabuleiros():
    print(ListaLetras + '     ' + ListaLetras)
    t = ''
    for i in range(10):
        if i <9:
            t += ' '+str(i+1)
        else:
            t += str(i+1)
        for j in MatrizObservada[i]:
            if j == 1:
                t += CORES['green']+'▓▓▓▓▓'+CORES['reset']
            elif j == 0:
                t += CORES['black']+'▓▓▓▓▓'+CORES['reset']
            elif j == -1:
                t += CORES['red']+'▓▓▓▓▓'+CORES['reset']
            elif j == -2:
                t += CORES['blue']+'▓▓▓▓▓'+CORES['reset']
        if i <9:
            t += ' '+str(i+1)
        else:
            t += str(i+1)
        t += '     '
        if i <9:
            t += ' '+str(i+1)
        else:
            t += str(i+1)
        for j in MatrizPlayer[i]:
            if j == 1:
                t += CORES['green']+'▓▓▓▓▓'+CORES['reset']
            elif j == 0:
                t += CORES['black']+'▓▓▓▓▓'+CORES['reset']
            elif j == -1:
                t += CORES['red']+'▓▓▓▓▓'+CORES['reset']
            elif j == -2:
                t += CORES['blue']+'▓▓▓▓▓'+CORES['reset']
        if i <9:
            t += ' '+str(i+1)+'\n'
        else:
            t += str(i+1)
    
    print(t)
    print(ListaLetras + '     ' + ListaLetras)

def foi_derrotado(m):
    for i in m:
        for j in i:
            if j == 1:
                return False
    return True

def ve_se_ganhou(matriz):
    for i in matriz:
        for j in i:
            if j == 1:
                return False
    return True

LpN = {
'A' : 1,
'B' : 2,
'C' : 3,
'D' : 4,
'E' : 5,
'F' : 6,
'G' : 7,
'H' : 8,
'I' : 9,
'J' : 10,
}
CORES = {
'reset': '\u001b[0m',
'red': '\u001b[31m',
'black': '\u001b[30m',
'green': '\u001b[32m',
'yellow': '\u001b[33m',
'blue': '\u001b[34m',
'magenta': '\u001b[35m',
'cyan': '\u001b[36m',
'white': '\u001b[37m'
}
ListaLetras = 'N   A    B    C    D    E    F    G    H    I    J   N'
Letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ListaNumeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

LP = ['Japão', 'Rússia', 'Austrália', 'França', 'Brasil']
PAISES =  {
    'Brasil': {
    'Cruzador': 1,
    'Torpedeiro': 2,
    'Destroyer': 1,
    'Couraçado': 1,
    'Porta-avioes': 1
    }, 
    'França': {
    'Cruzador': 3, 
    'Porta-avioes': 1, 
    'Destroyer': 1, 
    'Submarino': 1, 
    'Couraçado': 1
    },
    'Austrália': {
    'Couraçado': 1,
    'Cruzador': 3, 
    'Submarino': 1,
    'Porta-avioes': 1, 
    'Torpedeiro': 1
    },
    'Rússia': {
    'Cruzador': 1,
    'Porta-avioes': 1,
    'Couraçado': 2,
    'Destroyer': 1,
    'Submarino': 1
    },
    'Japão': {
    'Torpedeiro': 2,
    'Cruzador': 1,
    'Destroyer': 2,
    'Couraçado': 1,
    'Submarino': 1
    }
}

Barcos = {
'Destroyer': 3,
'Porta-avioes': 5,
'Submarino': 2,
'Torpedeiro': 3,
'Cruzador': 2,
'Couraçado': 4
}


MatrizPadrao = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

def DefineBarcosBot(pais_player):
    Matriz = MatrizPadrao
    pais_certo = True
    while pais_certo:
        p = random.choice(LP)
        pais_certo = p == pais_player
    print('O oponente vai jogar como {0}'.format(p))
    for barco in PAISES[p]: 
        Passou = True
        while Passou:
            linha = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            coluna = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            orientacao = random.choice(['h', 'v'])
            if orientacao == 'h':
                OverLap = False
                if Barcos[barco] + coluna <= 10:
                    for i in range(Barcos[barco]):
                        if Matriz[linha][coluna+i] != 0:
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(Barcos[barco]):
                            Matriz[linha][coluna+i] = 1
            elif orientacao == 'v':
                OverLap = False
                if Barcos[barco] + linha <= 10:
                    for i in range(Barcos[barco]):
                        if Matriz[linha+i][coluna] != 0:
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(Barcos[barco]):
                            Matriz[linha+i][coluna] = 1
    return Matriz

def Tiro(Matriz, Linha, Coluna):
    if Matriz[Linha-1][LpN[Coluna]-1] == -1 or Matriz[Linha-1][LpN[Coluna]-1] == -2:
        return 'Isso já foi selecionado\nTente novamente'
    elif Matriz[Linha-1][LpN[Coluna]-1] == 0:
        return 'Shuaaaaa ... água'
    elif Matriz[Linha-1][LpN[Coluna]-1] == 1:
        return 'BOOOOOM! Um navio foi acertado'

def DefineBarcos(pais_player):
    Matriz = MatrizPadrao
    print('Agora vamos posicionar os seus barcos.')
    print(ListaLetras)
    for i in range(len(Matriz)):
        if i <9:
            t = ' '+str(i+1)
        else:
            t = str(i+1)
        for j in Matriz[i]:
            if j == 1:
                t += CORES['green']+'▓▓▓▓▓'+CORES['reset']
            elif j == 0:
                t += CORES['black']+'▓▓▓▓▓'+CORES['reset']
            elif j == -1:
                t += CORES['red']+'▓▓▓▓▓'+CORES['reset']
            elif j == -2:
                t += CORES['blue']+'▓▓▓▓▓'+CORES['reset']
        if i <9:
            t += ' '+str(i+1)
        else:
            t += str(i+1)
        print(t)
    print(ListaLetras)
    for barco in PAISES[pais_player]:
        print('{0} possui {1} de tamanho'.format(barco, Barcos[barco]))
        Passou = True
        while Passou:
            #linha e coluna
            while True:
                posicao = input("Escolha onde será a posição (LN): ")
                if len(posicao) <2: 
                    print('Digitado errado')
                else:
                    linha = posicao[1]
                    coluna = posicao[0]
                    if len(posicao) == 3:
                        linha = posicao[1] + posicao[2]
                    if linha in ListaNumeros and coluna in Letras:
                        linha = int(linha)-1
                        coluna = LpN[coluna[0]]-1
                        break
                    else:
                        print('Digitado errado')
            
            #orientação
            orientacao = input('Qual orientação? (h ou v): ')
            if orientacao == 'h' or orientacao == 'H':
                OverLap = False
                if Barcos[barco] + coluna > 10:
                    print('Indisponível')
                else:
                    for i in range(Barcos[barco]):
                        if Matriz[linha][coluna+i] != 0:
                            print('Indisponível')
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(Barcos[barco]):
                            Matriz[linha][coluna+i] = 1
            elif orientacao == 'v' or orientacao == 'V':
                OverLap = False
                if Barcos[barco] + linha > 10:
                    print('Indisponível')
                else:
                    for i in range(Barcos[barco]):
                        if Matriz[linha+i][coluna] != 0:
                            print('Indisponível')
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(Barcos[barco]):
                            Matriz[linha+i][coluna] = 1
            else:
                print('Digitado errado')
        print(ListaLetras)
        for i in range(len(Matriz)):
            if i <9:
                t = ' '+str(i+1)
            else:
                t = str(i+1)
            for j in Matriz[i]:
                if j == 1:
                    t += CORES['green']+'▓▓▓▓▓'+CORES['reset']
                elif j == 0:
                    t += CORES['black']+'▓▓▓▓▓'+CORES['reset']
                elif j == -1:
                    t += CORES['red']+'▓▓▓▓▓'+CORES['reset']
                elif j == -2:
                    t += CORES['blue']+'▓▓▓▓▓'+CORES['reset']
            if i <9:
                t += ' '+str(i+1)
            else:
                t += str(i+1)
            print(t)
        print(ListaLetras)
    return Matriz

game = True
while game:
    # definir pais do player
    while True:
        pais_player = input('Qual país você quer ser? (Japão, Rússia, Austrália, França, Brasil): ')
        if pais_player in LP:
            break
        else:
            print('País Indisponível')
    MatrizPadrao = [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
    MatrizPlayer = DefineBarcos(pais_player)
    MatrizPadrao = [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
    MatrizBot = DefineBarcosBot(pais_player)

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
        # Pedir Tiro
        print('Sua vez de atirar!')
        nao_passou = True
        while nao_passou:
            errado = True
            while errado:
                tiro = input("Escolha onde será o tiro (LN): ")
                if len(tiro) <2: 
                    print('Digitado errado')
                else:
                    linha = tiro[1]
                    coluna = tiro[0]
                    if len(tiro) == 3:
                        linha = tiro[1] + tiro[2]
                    if linha in ListaNumeros and coluna in Letras:
                        linha = int(linha)
                        errado = False
                    else:
                        print('Digitado errado')

            if Tiro(MatrizBot, linha, coluna) == 'Isso já foi selecionado\nTente novamente':
                nao_passou = True
                print('Isso já foi selecionado\nTente novamente')
            elif Tiro(MatrizBot, linha, coluna) == 'Shuaaaaa ... água':
                print('Shuaaaaa ... água')
                MatrizBot[linha-1][LpN[coluna]-1] = -2
                MatrizObservada[linha-1][LpN[coluna]-1] = -2
                nao_passou = False
            else:
                print('BOOOOOM! Um navio foi acertado')
                MatrizBot[linha-1][LpN[coluna]-1] = -1
                MatrizObservada[linha-1][LpN[coluna]-1] = -1
                nao_passou = False
        mostra_tabuleiros()

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
            if Tiro(MatrizPlayer, linha, coluna) == 'Shuaaaaa ... água':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -2
                break
            elif Tiro(MatrizPlayer, linha, coluna) == 'BOOOOOM! Um navio foi acertado':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -1
                break
        mostra_tabuleiros()

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


# colocar de quem é cada matriz e (tipo matriz player e matriz computador) e qual país cada um escolheu - tipo o exemplo na academia python