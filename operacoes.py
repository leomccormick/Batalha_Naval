import random, time
from constantes import *

def agua():
    splash.play()
def boom():
    BOOM.play()

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

def mostra_tabuleiros(p: str, pais_player: str, MatrizObservada: list, MatrizPlayer: list) -> None:
    print('                   ' + 'OPONENTE - ' + p + '                                            ' + 'VOCÊ - ' + pais_player)
    print(ListaLetras + '     ' + ListaLetras)
    t = ''
    for i in range(10):
        if i <9:
            t += ' '+str(i+1)
        else:
            t += str(i+1)
        for j in MatrizObservada[i]:
            if j in indices_barcos:
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
            if j in indices_barcos:
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

def foi_derrotado(m: list) -> bool:
    for i in m:
        for j in i:
            if j == 1:
                return False
    return True

def ve_se_ganhou(matriz: list) -> bool:
    for i in matriz:
        for j in i:
            if j == 1:
                return False
    return True

def defineBarcosBot(p: str) -> list:
    Matriz = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    print('O oponente vai jogar como {0}'.format(p))
    for barco in PAISES[p]: 
        for i in range(PAISES[p][barco]):
            while True:
                linha = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                coluna = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                orientacao = random.choice(['h', 'v'])
                int_barco = indices[barco]
                while True:
                    encontrou_barco = False
                    for i in Matriz:
                        if int_barco in i:
                            int_barco = int_barco * 10
                            encontrou_barco = True
                            break
                    if not encontrou_barco:
                        break
                if orientacao == 'h':
                    OverLap = False
                    if Barcos[barco] + coluna <= 10:
                        for i in range(Barcos[barco]):
                            if Matriz[linha][coluna+i] != 0:
                                OverLap = True
                        if not OverLap:
                            for i in range(Barcos[barco]):
                                Matriz[linha][coluna+i] = int_barco
                            break
                elif orientacao == 'v':
                    OverLap = False
                    if Barcos[barco] + linha <= 10:
                        for i in range(Barcos[barco]):
                            if Matriz[linha+i][coluna] != 0:
                                OverLap = True
                        if not OverLap:
                            for i in range(Barcos[barco]):
                                Matriz[linha+i][coluna] = int_barco
                            break
    return Matriz

def tiros(Matriz: list, Linha: int, Coluna: str) -> str:
    if Matriz[Linha-1][LpN[Coluna]-1] == -1 or Matriz[Linha-1][LpN[Coluna]-1] == -2:
        return 'Isso já foi selecionado\nTente novamente'
    elif Matriz[Linha-1][LpN[Coluna]-1] == 0:
        return 'Shuaaaaa ... água'
    else:
        return 'BOOOOOM! Um navio foi acertado'
    
def barcoRestante(matriz: list, tipo_barco: int) -> bool:
    for i in matriz:
        if tipo_barco in i:
            return True
    return False

def defineBarcos(pais_player: str) -> list:
    Matriz = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    print('Agora vamos posicionar os seus barcos.')
    time.sleep(0.6)
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
        for i in range(PAISES[pais_player][barco]):
            time.sleep(0.3)
            print('{0} possui {1} de tamanho'.format(barco, Barcos[barco]))
            Passou = True
            while Passou:
                #linha e coluna
                while True:
                    time.sleep(0.3)
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
                        if not OverLap:
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
                        if not OverLap:
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