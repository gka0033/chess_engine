import board
turn = 1

def now_turn():
    if turn % 2 == 0:
        return 'b'
    else:
        return 'w'

def next_turn():
    global turn
    turn += 1

def turn_check(color):
    if color != now_turn():
        print('올바른 색이 아닙니다')
        return False
    return True

def is_check(color):

    king_pos = board.find_king(color)

    if king_pos is None:
        return False

    enemy = 'w' if color == 'b' else 'b'

    enemy_moves = board.get_all_moves(enemy)

    return king_pos in enemy_moves