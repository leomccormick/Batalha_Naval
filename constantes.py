# Valores e cores do mapa
# Vazio = Preto = 0
# Barco existente = Verde = 1
# Barco atingido = Vermelho = -1
# Água atingida = Azul = -2

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

ListaLetras = 'N   A    B    C    D    E    F    G    H    I    J   N'
Letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ListaNumeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

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