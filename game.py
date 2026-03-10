turn = 1

def now_turn():
    if turn % 2 == 0:
        return 'b'
    else:
        return 'w'

def next_turn():
    global turn
    turn += 1

