import board
# 현재 턴
turn = 1

# 현재 턴이 누구 차례인지 나타내는 함수
def now_turn_color():
    if turn % 2 == 0:
        return 'b'
    else:
        return 'w'

# 턴을 1회 진행시키는 함수
def next_turn():
    global turn
    turn += 1

# 사용자가 기물을 골랐을때, 그것이 올바른 턴(차례)인지 확인하는 함수
# 함수: now_turn()
def turn_check(color):
    if color != now_turn_color():
        print('올바른 색이 아닙니다')
        return False
    return True

# color 진형이 체크 상태인지 확인하는 함수
# 함수: find_king(), get_all_moves()
def is_check(color):

    king_pos = board.find_king(color)

    if king_pos is None:
        return False

    enemy = 'w' if color == 'b' else 'b'

    enemy_moves = board.get_all_moves(enemy)

    return king_pos in enemy_moves

# color 진형이 체크 상태인지 확인하는 함수
# 함수: get_color(), get_moves_can()
def is_checkmate(color):

    for y in range(1, 9):
        for x in range(1 , 9):
            
            if board.get_color(x, y) != color:
                continue
            
            if board.get_moves_can(x, y):
                return False

    return True