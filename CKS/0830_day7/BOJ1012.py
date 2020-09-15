def dfs(y, x):
    # 좌표간 이동 설정 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # stack 이용
    stack = [(y, x)]

    # stack이 비면 종료하겠다
    while len(stack):
        # 지나간 지점은 0으로 만들겠다
        arr[y][x] = 0
        # 상하좌우 이동해서 확인하겠다
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if 0 <= new_y < N and 0 <= new_x < M and arr[new_y][new_x]:
                # 해당 지점이 1이다(지나가지 않았다)
                stack.append((y, x))
                y += dy[i]
                x += dx[i]
                break

        else:
            # 찾는 지점이 없다면 뒤로 돌아가서 보겠다
             y, x = stack.pop()



T = int(input())    # test case

for tc in range(1, T + 1):

    # M : 가로 길이, N : 세로 길이, K : 배추 좌표 개수
    M, N, K = map(int, input().split())

    # 배추의 위치 그리기
    arr = [[0] * M for _ in range(N)]

    # 인접행렬 그리기
    adj_matrice = [[0] * M for _ in range(N)]

    # 인접행렬에 배추 위치 배정
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # 최종 지렁이 수 세기
    cnt = 0


    # DFS 실시 / 전체 탐색
    for y in range(N):
        for x in range(M):
            # 배추위치이고 방문하지 않았다면
            if arr[y][x] == 1 and adj_matrice[y][x] == 0:
                cnt += 1
                dfs(y, x)

    print(cnt)