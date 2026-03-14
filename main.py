# TODO: 코드 재정리 및 구조 정리 필요
# v0.5 주석 처리. 
# 2026-03-14
# 스태일매이트 완성
# NOTE: 현 board.이동 관련 함수에 대해 고민중

import board
import game

s = input('prass any button to start')
game.game_on()

## 보드 생성
boardnow = board.init_board()
s = ''
while game.on:
    
    ## 보드 출력 코드
    board.board_print(boardnow)
    ## 정보판 표시
    print(f'현재 턴수 {game.turn}')
    print("기물을 입력하세요 ex 12, 58, 97")
    print("'s'를 눌러 취소합니다")

    # 기물 선택 입력
    s = board.player_input()
    if s == 'end':
        print('종료합니다')
        break
    elif s == 'back':
        print('올바른 입력이 아닙니다')
        break

    # s값 분해
    # 이후 x1와 y1로 나눔
    x1, y1 = game.input_decom(s)
    
    # 현재 올바른 진형을 골랐는지 체크
    my_color = board.get_color(x1, y1)
    if my_color is None:
        print("기물이 없습니다.")
        continue
    enemy_color = 'w' if my_color == 'b' else 'b'
    print(my_color, enemy_color)
    if not game.turn_check(my_color):
        continue

    # 고른 기물의 모든 움직일수 있는 경우의 수
    piece_moves =  board.get_moves_can(x1, y1)
    print(piece_moves)

    #목적지 입력
    if piece_moves:
        print("목적지를 입력하세요 ex 12, 58, 97")
        print("'s'를 눌러 취소합니다")
        d = board.player_input()
        if d == 'end':
            print('종료합니다')
            break
        elif d == 'back':
            print('올바른 입력이 아닙니다')
            break
        x2, y2 = game.input_decom(d)
        
        # 기물 이동
        if (x2, y2) in piece_moves:
            board.move(x1, y1, x2, y2)

            game.after_move(my_color, enemy_color)


    else:
        print("올바른 입력이 아닙니다.")
        continue
    
    
    

  