import pieces
import game

# 선택한 좌표의 기물 반환
# return '??'(기물) or '..'
def select(x, y):
    return board[y][x]

# 선택한 좌표 기물의 색 반환
def get_color(x, y):
    if is_empty(x, y):
        return None
    
    piece = select(x, y)
    return piece[0]

# 선택한 좌표가 보드 안인지 반환
# True 보드 안임, False 보드 밖임
def is_inside_board(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

# 지정 좌표에 지정 기물을 생성
def set_piece(x, y, piece):
    board[y][x] = piece

# 보드 생성
# 지금은 맘대로 수정해서 실험하자
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
    board[1][5] = 'wK'
    board[8][1] = 'bQ'
    board[8][2] = 'bQ'


    return board

# 좌표가 비어있는지 확인하는 함수
def is_empty(x, y):
    if not is_inside_board(x, y):
        return False
    
    return select(x, y) == '..'

# 좌표에 있는 기물이 적인지 판단하는 함수
# return True 적, False 아님
def is_enemy(x, y, color):
    if not is_inside_board(x, y):
        return False
    
    piece = select(x, y)
    if is_empty(x, y):
        return False
    return color != piece[0]
# 좌표에 있는 기물이 아군인지 판단하는 함수
# return True 아군, False 적
def is_friend(x, y, color):
    if not is_inside_board(x, y):
        return False
    
    piece = select(x, y)
    if is_empty(x, y):
        return False
    return color == piece[0]


# 기물을 실제로 움직이는 함수
# x1, y1 을 x2, y2 로 이동후 x1, y1 은 '..'
# 함수: game.next_turn()
def move(x1, y1, x2, y2):
    piece = select(x1, y1)
    set_piece(x2, y2, piece)
    set_piece(x1, y1, '..')
    
# 기물이 움직일수 있는 수를 반환하는 함수
# retrun 이동 가능한 좌표 리스트
# 함수 select(), pieces.기물이름_moves()
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

# 한 진형의 모든 움직임 수를 반환하는 함수
# 1,1 - 8,8까지 color 진형의 모든 이동의 수 반환
# return moves 
# 함수 select(), get_moves()
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

# 테스트용 이동
# 이동은 move()와 같음
# return x2, y2 에 있던 기물 정보. 후에 타 함수에서 사용(undo처럼)
# 함수: select(), set_piece
def simulate_move(x1, y1, x2, y2):
    piece = select(x1, y1)
    captured = select(x2, y2)
    set_piece(x2, y2, piece)
    set_piece(x1, y1, '..')
    return captured

# 기물 이동을 취소
# !이동은 x2, y2 -> x1, y1 순서임!
# 함수: select(), set_piece()
def undo_move(x1, y1, x2, y2, captured):
    piece = select(x2, y2)
    set_piece(x2, y2, captured)
    set_piece(x1, y1, piece)

# 움직일수 있는 경우의 수를 반환하는 함수
# simulate_move()를 했을때, 체크인 경우는 제외함
# return moves_can
# 함수: get_moves(), get_color(), simulate_move(), is_check, undo_move()
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

# color 진형의 왕의 위치를 반환하는 함수
# 1-9, 1-9 까지의 모든 수 체크
# return (x,y) K의 위치
# 함수: select()
def find_king(color):
    target = color + 'K'

    for y in range(1,9):
        for x in range(1,9):
            if select(x,y) == target:
                return (x,y)

    return None