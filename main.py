import board
import game
## 보드 생성

boardnow = board.init_board()



s = ''
while s != 's':
    
    ## 보드 출력 코드
    print('')
    for row in boardnow:
        print(" ".join(row))
    print('')
    print(f'현재 턴수 {game.turn}')
    print("기물을 입력하세요 ex 12, 58, 97")
    print("'s'를 눌러 취소합니다")

    # 기물 선택 입력
    s = input(">")

    if s == 's':
        print('종료됩니다.')
        break
    elif len(s) < 2 or not s[0].isdigit() or not s[1].isdigit():
        print("올바른 입력이 아닙니다.")
        continue

    # s값 분해
    ls = list(s)
    x1, y1 = (int(ls[0]),int(ls[1]))
    print(x1, y1)
    
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
        d= input(">")
        if d == 's':
            print('취소합니다')
            continue
        elif len(d) < 2 or not d[0].isdigit() or not d[1].isdigit():
            print("올바른 입력이 아닙니다.")
            continue
        ld = list(d)
        x2, y2 = (int(ld[0]),int(ld[1]))
        
        # 기물 이동
        if (x2, y2) in piece_moves:
            board.move(x1, y1, x2, y2)

            # 체크 상태 확인
            if game.is_check(enemy_color):
                print('체크!')
                if game.is_checkmate(enemy_color):
                    print('체크메이트, 승리!')
                    break
            game.next_turn()


    else:
        print("올바른 입력이 아닙니다.")
        continue
    
    
    

  