# dfs 실시
def dfs(y, x):
    # 8방향 이동 구현
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1. -1, 0, 1, 1, 1, 0, -1]

    # 좌표 아래로 이동시켜서 위치를 구하자 (그 전 위치 정보 저장)
    # 마지막까지 가면 다시 reset 시켜야 함
    while
    # 이동시켜서 배치할 수 있나 확인해보자
    for i in range(8):
        new_y, new_x = y + dy[i], x + dx[i]
        while 0 <= new_y < N and 0 <= new_x < N:
            if not arr[new_y][new_x]:
                # 끝까지 가서 확인해보자
                new_y += dy[i]
                new_x += dx[i]


N = 8

# 퀸을 놓는 방법의 수 구하기 / 배열 생성
arr = [[0] * N for _ in range(N)]

# 첫 행에서 퀸 배열하자 => 마지막 열에 위치하면 끝내고 개수 구하기
for i in range(N):
    # 1이 아닐 때
    if not arr[0][i]:
        arr[0][i] = 1
        dfs(0, i)
