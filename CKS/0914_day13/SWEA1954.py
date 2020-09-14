# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 0. 우, 아래, 좌, 위 순서로 벽을 만나면 이동방향 회전
    arr = [[0]* N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 1. 시작좌표  => 첫 시작값을 정해놓고 시작하는 게 while문 조건 주기 편하다
    new_y, new_x = 0, 0
    cnt = 1
    i = 0
    arr[new_y][new_x] = cnt
    cnt += 1

    # 2. N^2의 수가 들어가면 모두 다 들어간 것
    while cnt <= (N ** 2):
        # 2. 조건 설정 => 해당 방향에서 조건에서 벗어나서 밖의 while문으로 나오면 방향전환 실시
        new_y = new_y +dy[i]
        new_x = new_x +dx[i]

        # 해당 진행방향 동안 증가
        while 0 <= new_y < N and 0 <= new_x < N and not arr[new_y][new_x]:
            arr[new_y][new_x] = cnt
            cnt += 1
            new_y = new_y + dy[i]
            new_x = new_x + dx[i]

        # 해당 진행방향이 끝났다 => 그 전 좌표로 돌려보내고 방향 전환(while문이 끝나면 조건이 맞지 않는다)
        new_y = new_y - dy[i]
        new_x = new_x - dx[i]
        # 인덱스 범위 벗어나지 않게 설정
        i = (i + 1) % 4

    # 출력
    print('#{}'.format(tc))
    for i in range(len(arr)):
        print(' '.join(map(str, arr[i])))