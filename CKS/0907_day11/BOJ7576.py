# https://www.acmicpc.net/problem/7576

# 시행이 끝났는데 모두 익지 못하는 경우 판별
def checkripe(arr, k):

    cnt_days = 0

    for y in range(N):
        cnt_days += arr[y].count(0)

    # 1. 0이 없다 => 다 익었다
    if cnt_days == 0:
        return k

    else:
        return -1

# 익은 토마토가 2개 이상일 경우가 있을 수 있음 - for문 탐색 시 확인해줘야 함
def countripe(arr):
    # bfs를 실시할 좌표
    axes = []

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                # 첫 시행이므로
               axes.append((y, x, 0))

    return axes

# bfs 생성
def bfs(list):
    # queue 생성
    queue = []

    # 튜플 형태로 저장
    for i in range(len(list)):
        queue.append(list[i])

    # 상하좌우 구현
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        y, x, k = queue.pop(0)

        # 이동시켜서 익는 부분 탐색
        for i in range(4):
            new_y, new_x = y + dy[i], x + dx[i]

            # 범위 안 넘어가게
            if  0 <= new_y < N and 0 <= new_x < M:
                # 갈 수 있는 부분이면 바꿔주고 큐에 넣자
                if arr[new_y][new_x] == 0:
                    arr[new_y][new_x] = 1
                    queue.append((new_y, new_x, k + 1))

    # 출력 조건 생성
    result = checkripe(arr, k)

    return result


M, N = map(int, input().split())    # N행 M열 박스 크기

# 토마토의 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 모든 토마토 익은 경우 거르기 위한 변수
days = 0

# 1-1. 저장될 때 모든 토마토가 익어 있는 경우
for y in range(N):
    days += arr[y].count(0)

if not days:
    print(0)

else:
    result = countripe(arr)
    result = bfs(result)
    print(result)
