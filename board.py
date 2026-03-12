import pieces
import game
def select(x, y):
    return board[y][x]

def get_color(x, y):
    piece = select(x, y)
    if piece == '..':
        return None
    return piece[0]
def is_inside_board(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

def set_piece(x, y, piece):
    board[y][x] = piece

def init_board():
    global board
    board = []
    for y in range(9):
        row = []
        for x in range(9):
            if x == 0:
                row.append(str(y))
            elif y == 0:
                row.append('0' + str(x))
            else:
                row.append('..')
        board.append(row)
    '''
    for i in range(1,9):
        board[7][i] = 'bP'
        board[2][i] = 'wP'

    board[8][2] = 'bN'
    board[8][7] = 'bN'
    board[8][1] = 'bR'
    board[8][8] = 'bR'
    board[8][3] = 'bB'
    board[8][6] = 'bB'
    board[8][4] = 'bK'
    board[8][5] = 'bQ'
    board[1][2] = 'wN'
    board[1][7] = 'wN'
    board[1][1] = 'wR'
    board[1][8] = 'wR'
    board[1][3] = 'wB'
    board[1][6] = 'wB'
    board[1][4] = 'wK'
    board[1][5] = 'wQ'
    '''

    board[8][5] = 'bK'
    board[1][2] = 'wQ'
    board[1][7] = 'wQ'
    board[1][1] = 'wQ'
    board[1][8] = 'wQ'
    board[1][3] = 'wQ'
    board[1][6] = 'wQ'
    board[1][4] = 'wQ'
    board[1][5] = 'wQ'

    return board

def is_empty(x, y):
    return is_inside_board(x, y) and select(x, y) == '..' 

def is_enemy(x, y, color):
    if not is_inside_board(x, y):
        return False
    
    piece = select(x, y)
    if piece == '..':
        return False
    return color != piece[0]

def is_friend(x, y, color):
    if not is_inside_board(x, y):
        return False
    
    piece = select(x, y)
    if piece == '..':
        return False
    return color == piece[0]



def move(x1, y1, x2, y2):
    piece = select(x1, y1)
    set_piece(x2, y2, piece)
    set_piece(x1, y1, '..')
    game.next_turn()
    
def get_moves(x, y):
    piece = select(x, y)
    if piece == '..':
        return []
    
    color = piece[0]
    kind = piece[1]

    if kind == 'P':
        return pieces.pawn_moves(x, y, color) + pieces.pawn_attacks(x, y, color)
    if kind == 'N':
        return pieces.knight_moves(x, y, color)
    if kind =='R':
        return pieces.rook_moves(x, y, color)
    if kind == 'B':
         return pieces.bishop_moves(x, y, color)
    if kind == 'Q':
        return pieces.queen_moves(x, y, color)
    if kind =='K':
        return pieces.king_moves(x, y, color)

    return []

def get_all_moves(color):
    moves = []

    for y in range(1,9):
        for x in range(1,9):
            piece = select(x,y)

            if piece == '..':
                continue

            if piece[0] != color:
                continue

            piece_moves = get_moves(x,y)

            for m in piece_moves:
                moves.append(m)

    return moves

def simulate_move(x1, y1, x2, y2):
    piece = select(x1, y1)
    captured = select(x2, y2)
    set_piece(x2, y2, piece)
    set_piece(x1, y1, '..')

    return captured

def undo_move(x1, y1, x2, y2, captured):
    piece = select(x2, y2)
    set_piece(x2, y2, captured)
    set_piece(x1, y1, piece)

def get_moves_can(x, y):
    moves = get_moves(x, y)
    moves_can = []
    color = get_color(x, y)

    for (mx, my) in moves:
        captured = simulate_move(x, y, mx, my)
        if game.is_check(color):
            undo_move(x, y, mx, my, captured)
        else:
            moves_can.append((mx, my))
            undo_move(x, y, mx, my, captured)
    return moves_can

def find_king(color):
    target = color + 'K'

    for y in range(1,9):
        for x in range(1,9):
            if select(x,y) == target:
                return (x,y)

    return None