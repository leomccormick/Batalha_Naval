import random

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
        for barco in Barcos:
            Passou = True
            while Passou:
                linha = random.choice([0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9])
                coluna = random.choice([0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9])
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
            return 'Isso já foi selecionado'
        elif Matriz[Linha-1][LpN[Coluna]-1] == 0:
            return 'água'
        elif Matriz[Linha-1][LpN[Coluna]-1] == 1:
            return 'navio'

    def DefineBarcos():
        Matriz = MatrizPadrao
        Y = True
        while Y:
            pais = input('Qual país você quer ser? (Japão, Rússia, Austrália, França, Brasil) : ')
            if pais in LP:
                Y = False
            else:
                print('País indisponível')
        for barco in PAISES[pais]:
            print('{0} possui {1} de tamanho'.format(barco, Barcos[barco]))
            Passou = True
            while Passou:
                linha = int(input('Qual linha? (1 - 10) : ')) - 1
                coluna = LpN[input('Qual linha? (A - J) : ')] - 1
                orientacao = input('Qual orientação? (h ou v) : ')
                if orientacao == 'h':
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
                elif orientacao == 'v':
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
    for i in range(len(MatrizBot)):
        print([[i+1]], [MatrizBot[i]],[[i+1]], [MatrizPlayer[i]], [[i+1]])
    #while Acao:
        # Mostrar Tabuleiro
        # Pedir Tiro
        # Mostrar Tabuleiro
        # Ver se Player ganhou - Acao = False
        # Tiro do Bot
        # Ver se Bot ganhou - Acao = False
        #x = 0
    
    game = input('Jogar novamente? (Sim ou Não) : ') == 'Sim'