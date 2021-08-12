from time import sleep

notacaoAlgebrica = [
        ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
        ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
    ]

def limite(i):
    return i > -1 and i < 8


def movimentosForaLimite(board, r, c, moves):
    board[r][c] = 0
    for move in moves:
        if (limite(move["r"] + r) and (limite(move["c"] + c))):
            board[r][c] += 1


def estadoInicial(moves):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]



    for r in range(0, 8):
        for c in range(0, 8):
            movimentosForaLimite(board, r, c, moves)
    return board


def tour(r, c, moves, moveNumber, board):
    if (moveNumber > 64):
        return

    nextR = 0
    nextC = 0
    minimoForaSaida = 9

    for move in moves:
        candidatoR = move["r"] + r
        candidatoC = move["c"] + c

        if (limite(candidatoR) and limite(candidatoC) and board[candidatoR][candidatoC] < minimoForaSaida):
            minimoForaSaida = board[candidatoR][candidatoC]
            nextR = candidatoR
            nextC = candidatoC

    board[r][c] = 100

    for move in moves:
        neighborR = move['r'] + r
        neigborC = move['c'] + c

        if (limite(neighborR) and limite(neigborC)):
           board[neighborR][neigborC]-=1

    sleep(0.5)
    print(notacaoAlgebrica[r][c])

    tour(nextR, nextC, moves, moveNumber + 1, board)

    amzR = []
    amzC = []

    amzR.append(r)
    amzC.append(c)

    if amzR and amzC == (nextR, nextC):
        print("DUPLICADO")


moves = [
    {"r": 2, "c": 1},
    {"r": 1, "c": 2},
    {"r": -1, "c": 2},
    {"r": -2, "c": 1},
    {"r": -2, "c": -1},
    {"r": -1, "c": -2},
    {"r": 1, "c": -2},
    {"r": 2, "c": -1},
]

parametro = input()
parametro = parametro.split(" ")

pegarY = 0
pegarX = 0

for i in range(0,8):
    for j in range(0 , 8):
        if(parametro[1] in notacaoAlgebrica[i][j]):
            pegarY = i
            pegarX = j

board = estadoInicial(moves)
tour(pegarY, pegarX, moves, 1, board)
