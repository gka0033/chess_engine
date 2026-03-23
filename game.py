import board
# 현재 턴
turn = 1
on = False
def game_on():
    global on
    on = True

def game_off():
    global on 
    on = False
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

# color 진형이 체크메이트 상태인지 확인하는 함수
# 함수: get_color(), get_moves_can()
def is_checkmate(color):

    for y in range(1, 9):
        for x in range(1 , 9):
            
            if board.get_color(x, y) != color:
                continue
            
            if board.get_moves_can(x, y):
                return False

    return True

# 프로모션 진행 함수
# 프로모션 실행 상태를 return 함
def promotion(x, y):
    piece = board.select(x, y)
    kind = piece[1]
    color = piece[0]
    if kind != 'P':
        return False
    
    if color == 'b':
        end = 1
    else:
        end = 8

    if y == end:
        board.set_piece(x, y, color+'Q')
        return True
    return False
    

# color 진형이 스테일메이트 상태인지 확인하는 함수
# 함수: get_color(), get_moves_can()
def is_stalemate(color):
    for y in range(1, 9):
        for x in range(1 , 9):
            
            if board.get_color(x, y) != color:
                continue
            
            if board.get_moves_can(x, y):
                return False

    return True

# 플레이어의 입력을 좌표로 반환
def input_decom(s):
    ls = list(s)
    x, y = (int(ls[0]),int(ls[1]))
    return x, y

# 이동후 판정을 확인하는 함수
def after_move(my_color, enemy_color):
    # 체크 상태 확인
    if is_check(enemy_color):
        print('체크!')
        # 체크메이트 확인
        if is_checkmate(enemy_color):
            print('체크메이트, 승리!')
            game_off()
    elif is_stalemate(enemy_color):
        print(f'{enemy_color}스테일메이트, 무승부')
        game_off()
    elif is_stalemate(my_color):
        print(f'{my_color}스테일메이트, 무승부')
        game_off()
    next_turn()