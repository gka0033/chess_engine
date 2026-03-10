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

    piece =  board.get_moves(x1, y1)
    print(piece)

    if piece:
        print("목적지를 입력하세요 ex 12, 58, 97")
        print("'s'를 눌러 취소합니다")
        d= input(">")
        ld = list(d)
        x2, y2 = (int(ld[0]),int(ld[1]))

        if (x2, y2) in piece:
            board.move(x1, y1, x2, y2)

    else:
        print("올바른 입력이 아닙니다.")
        continue
    
    
    

  