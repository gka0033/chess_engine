def select(x, y):
    return board[y][x]

def is_inside_board(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

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

def set_piece(x, y, piece):
    board[y][x] = piece

def move(x1, y1, x2, y2):
    piece = select(x1, y1)
    set_piece(x2, y2, piece)
    set_piece(x1, y1, '..')
    
def get_moves(x, y):
    piece = select(x, y)
    color = piece[0]
    kind = piece[1]
    if kind == 'P':
        return pawn_moves(x, y, color)
    if kind == 'N':
        return knight_moves(x, y, color)
    if kind =='R':
        return rook_moves(x, y, color)
    if kind == 'B':
         return bishop_moves(x, y, color)
    if kind == 'Q':
        return queen_moves(x, y, color)
    if kind =='K':
        return king_moves(x, y, color)

    return []
    
def pawn_moves(x, y, color):
    moves = []
    if color == 'b':
        start_row = 7
        dir = -1
    else:
        start_row = 2
        dir = 1

    is_first_move = y == start_row

    if is_empty(x, y+dir):
        moves.append((x,y+dir))
    if is_enemy(x+1, y+dir, color):
        moves.append((x+1, y+dir))
    if is_enemy(x-1, y+dir, color):
        moves.append((x-1, y+dir))
    if is_first_move and is_empty(x, y+dir) and is_empty(x, y+(dir * 2)):
        moves.append((x, y+dir*2))
    return moves

def knight_moves(x, y, color):
    moves = []
    allmoves = [(x+1,y+2), (x-1,y+2), (x+2,y+1), (x-2,y+1),
                (x+1,y-2), (x-1,y-2), (x+2,y-1), (x-2,y-1)]
    

    for am in allmoves:
        nx, ny = am
        if not is_inside_board(nx, ny):
            continue
        if is_empty(nx, ny) or is_enemy(nx, ny, color):
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

            if is_empty(nx, ny):
                moves.append((nx, ny))
            elif is_enemy(nx, ny, color):
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

            if is_empty(nx, ny):
                moves.append((nx, ny))
            elif is_enemy(nx, ny, color):
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
        if is_empty(nx, ny) or is_enemy(nx, ny, color):
            moves.append(am)
    return moves




## 보드 생성

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



s = ''
while s != 's':
    
    ## 보드 출력 코드
    print('')
    for row in board:
        print(" ".join(row))
    print('')
    
    print("기물을 입력하세요 ex 12, 58, 97")
    print("'s'를 눌러 취소합니다")
    s = input(">")

    if s == 's':
        print('종료됩니다.')
        break
    elif len(s) < 2 or not s[0].isdigit() or not s[1].isdigit():
        print("올바른 입력이 아닙니다.")
        continue

    ls = list(s)
    x1, y1 = (int(ls[0]),int(ls[1]))
    print(x1, y1)

    moves =  get_moves(x1, y1)
    print(moves)

    if moves:
        print("목적지를 입력하세요 ex 12, 58, 97")
        print("'s'를 눌러 취소합니다")
        d= input(">")
        ld = list(d)
        x2, y2 = (int(ld[0]),int(ld[1]))

        if (x2, y2) in moves:
            move(x1, y1, x2, y2)

    else:
        print("올바른 입력이 아닙니다.")
        continue
    
    
    

  