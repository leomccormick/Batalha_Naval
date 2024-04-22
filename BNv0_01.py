import random

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

def ve_se_ganhou(matriz):
    for i in matriz:
        for j in i:
            if j == 1:
                return False
    return True

game = True
while game:

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

    LP = ['Japão', 'Rússia', 'Austrália', 'França', 'Brasil']
    PAISES =  {
        'Brasil': {
            'cruzador': 1,
            'torpedeiro': 2,
            'destroyer': 1,
            'couracado': 1,
            'porta-avioes': 1
        }, 
        'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
        },
        'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
        },
        'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
        },
        'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
        }
    }

    Barcos = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
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

    def DefineBarcosBot():
        Matriz = MatrizPadrao
        p = random.choice(LP)
        print('O inimigo irá de {0}'.format(p))
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

    def DefineBarcos():
        Matriz = MatrizPadrao
        Y = True
        while Y:
            pais = input('Qual país você quer ser? (Japão, Rússia, Austrália, França, Brasil): ')
            if pais in LP:
                Y = False
            else:
                print('País indisponível')
        print('Agora vamos posicionar os seus barcos.')
        for barco in PAISES[pais]:
            print('{0} possui {1} de tamanho'.format(barco, Barcos[barco]))
            Passou = True
            while Passou:
                linha = int(input('Qual linha? (1 - 10) : ')) - 1
                coluna = LpN[input('Qual linha? (A - J) : ')] - 1
                orientacao = input('Qual orientação? (h ou v): ')
                if orientacao == 'h' or orientacao == 'H':
                    OverLap = False
                    if Barcos[barco] + coluna > 10:
                        print('indisponível')
                    else:
                        for i in range(Barcos[barco]):
                            if Matriz[linha][coluna+i] != 0:
                                print('indisponível')
                                OverLap = True
                        if OverLap == False:
                            Passou = False
                            for i in range(Barcos[barco]):
                                Matriz[linha][coluna+i] = 1
                elif orientacao == 'v' or orientacao == 'V':
                    OverLap = False
                    if Barcos[barco] + linha > 10:
                        print('indisponível')
                    else:
                        for i in range(Barcos[barco]):
                            if Matriz[linha+i][coluna] != 0:
                                print('indisponível')
                                OverLap = True
                        if OverLap == False:
                            Passou = False
                            for i in range(Barcos[barco]):
                                Matriz[linha+i][coluna] = 1
                else:
                    print('indisponível')
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

    MatrizPlayer = DefineBarcos()
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
    MatrizBot = DefineBarcosBot()

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
    Acao = True
    
    while Acao:
        # Pedir Tiro
        print('Sua vez de atirar!')
        nao_passou = True
        while nao_passou:
            linha = int(input('Escolha uma linha (1-10): '))
            coluna =  LpN[input('Escolha uma linha (A-J): ')]
            if Tiro(MatrizBot, linha, coluna) == 'Isso já foi selecionado\nTente novamente':
                nao_passou = True
                print('Isso já foi selecionado\nTente novamente')
            elif Tiro(MatrizBot, linha, coluna) == 'Shuaaaaa ... água':
                print('Shuaaaaa ... água')
                MatrizBot[linha-1][LpN[coluna]-1] = -2
                MatrizObservada[linha-1][LpN[coluna]-1] = -2
            else:
                print('BOOOOOM! Um navio foi acertado')
                MatrizBot[linha-1][LpN[coluna]-1] = -1
                MatrizObservada[linha-1][LpN[coluna]-1] = -1
        mostra_tabuleiros()
        # Ver se Player ganhou - Acao = False
        # Tiro do Bot
        print('Vez do seu oponente atirar...')
        nao_passou = True
        while nao_passou:
            linha = random.choice(range(1, 11))
            coluna =  random.choice(Letras)
            if Tiro(MatrizPlayer, linha, coluna) == 'Isso já foi selecionado\nTente novamente':
                nao_passou = True
            elif Tiro(MatrizPlayer, linha, coluna) == 'Shuaaaaa ... água':
                MatrizPlayer[linha-1][LpN[coluna]-1] = -2
            else:
                MatrizPlayer[linha-1][LpN[coluna]-1] = -1
        mostra_tabuleiros()
        # Ver se Bot ganhou - Acao = False
    
    game = input('Jogar novamente? (Sim ou Não): ') == 'Sim'