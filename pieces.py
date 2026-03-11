import board

def pawn_moves(x, y, color):
    moves = []
    if color == 'b':
        start_row = 7
        dir = -1
    else:
        start_row = 2
        dir = 1

    is_first_move = y == start_row

    if board.is_empty(x, y+dir):
        moves.append((x,y+dir))
    
    if is_first_move and board.is_empty(x, y+dir) and board.is_empty(x, y+(dir * 2)):
        moves.append((x, y+dir*2))
    return moves

def pawn_attacks(x, y, color):
    moves = []
    if color == 'b':
        dir = -1
    else:
        dir = 1
        
    if board.is_enemy(x+1, y+dir, color):
        moves.append((x+1, y+dir))
    if board.is_enemy(x-1, y+dir, color):
        moves.append((x-1, y+dir))

    return moves

def knight_moves(x, y, color):
    moves = []
    allmoves = [(x+1,y+2), (x-1,y+2), (x+2,y+1), (x-2,y+1),
                (x+1,y-2), (x-1,y-2), (x+2,y-1), (x-2,y-1)]
    

    for am in allmoves:
        nx, ny = am
        if not board.is_inside_board(nx, ny):
            continue
        if board.is_empty(nx, ny) or board.is_enemy(nx, ny, color):
            moves.append(am)

    return moves

def rook_moves(x, y, color):
    moves = []
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx, dy in dir:
        i = 1
        while True:
            nx = x + dx*i
            ny = y + dy*i

            if board.is_empty(nx, ny):
                moves.append((nx, ny))
            elif board.is_enemy(nx, ny, color):
                moves.append((nx, ny))
                break
            else:
                break
            i += 1
    return moves

def bishop_moves(x, y, color):
    moves = []
    dir = [(1,1),(-1,1),(1,-1),(-1,-1)]
    for dx, dy in dir:
        i = 1
        while True:
            nx = x + dx*i
            ny = y + dy*i

            if board.is_empty(nx, ny):
                moves.append((nx, ny))
            elif board.is_enemy(nx, ny, color):
                moves.append((nx, ny))
                break
            else:
                break
            i += 1
    return moves

def queen_moves(x, y, color):
    return rook_moves(x, y, color) + bishop_moves(x, y, color)

def king_moves(x, y, color):
    moves = []
    allmoves = [(x+1,y), (x+1,y+1), (x,y+1), (x-1,y+1),
                (x-1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]
    for am in allmoves:
        nx, ny = am
        if board.is_empty(nx, ny) or board.is_enemy(nx, ny, color):
            moves.append(am)
    return moves