# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE

import sys
sys.stdin = open('1974.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = 9
    # 스도쿠 퍼즐판
    brd = [list(map(int, input().split())) for _ in range(N)]

    # 검증에 사용할 판 생성
    valid_li = [0] * 10
    flag = True

    # 1. 가로 검증
    for y in range(N):
        for x in range(N):
            valid_li[brd[y][x]] = 1

        # 한 행의 탐색이 끝났을 때 스도쿠 조건에 맞는지 확인
        if sum(valid_li) != 9:
            flag = False
            break

        valid_li = [0] * 10

    if flag:
        # 2. 세로 검증
        for x in range(N):
            for y in range(N):
                valid_li[brd[y][x]] = 1

            # 한 행의 탐색이 끝났을 때 스도쿠 조건에 맞는지 확인
            if sum(valid_li) != 9:
                flag = False
                break
            valid_li = [0] * 10
    if flag:
        # 3. 작은 사각형 검증
        for y in range(0, 7, 3):
            if not flag:
                break
            for x in range(0, 7, 3):
                start_y, start_x = y, x

                for i in range(3):
                    for j in range(3):
                        valid_li[brd[start_y + i][start_x + j]] = 1

                if sum(valid_li) != 9:
                    flag = False
                    break
                valid_li = [0] * 10

    # 4. 조건 확인 후 출력
    print('#{}'.format(tc), end=' ')
    if flag:
        print(1)

    else:
        print(0)
