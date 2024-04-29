# Valores e cores do mapa
# Vazio = Preto = 0
# Barco existente = Verde = 1
# Barco atingido = Vermelho = -1
# Água atingida = Azul = -2
from pygame import mixer

mixer.init()

BOOM = mixer.Sound("Explosao.mp3")
splash = mixer.Sound("Splash.mp3")

indices = {
'Destroyer': 1,
'Porta-avioes': 2,
'Submarino': 3,
'Torpedeiro': 4,
'Cruzador': 5,
'Couraçado': 6 
}

n_barco = {
1: 'Destroyer',
2: 'Porta-avioes',
3: 'Submarino',
4: 'Torpedeiro',
5: 'Cruzador',
6: 'Couraçado',
}

indices_barcos = [1, 2, 3, 4, 5, 6]

indices_possiveis = [1, 2, 3, 4, 5, 6, 1*10, 2*10, 3*10, 4*10, 5*10, 6*10, 1*100, 2*100, 3*100, 4*100, 5*100, 6*100]

# Tamanho dos barcos
Barcos = {
'Destroyer': 3,
'Porta-avioes': 5,
'Submarino': 2,
'Torpedeiro': 3,
'Cruzador': 2,
'Couraçado': 4
}

# Frota de cada país com a qnt de barcos
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

ListaLetras = 'N   A    B    C    D    E    F    G    H    I    J   N'
Letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ListaNumeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Lista de países
LP = ['Japão', 'Rússia', 'Austrália', 'França', 'Brasil']

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