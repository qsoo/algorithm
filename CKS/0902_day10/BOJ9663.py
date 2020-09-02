# https://www.acmicpc.net/problem/9663


def ispossible(y, x):
    # 이동시켜서 확인하자(8방향)
    dx_1 = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy_1 = [-1, -1, -1, 0, 0, 1, 1, 1]

    dx = [1, 0, 1, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, 0, -1, 1, 1, 1]


    # 1. 가로 / 세로 / 대각선
    for i in range(8):
        new_y, new_x = y + dy[i], x + dx[i]
        while 0 <= new_y < N and 0 <= new_x < N:
            if not arr[new_y][new_x]:
                new_y += dy[i]
                new_x += dx[i]


            else:
                return False
                break
            break

    return True

'''
현재 행 탐색을 안하고 그냥 열에서 밑으로만 내려와서 퀸 배치여부를 본다 
=> 행 탐색을 할 수 있게 dfs 함수 부분 수정 필요
'''


def dfs(y, x):
    global k
    global cnt
    print('dfs시작', y, x)
    # 종료조건
    if k == N:
        cnt += 1
        print(cnt)
    # 진행조건
    elif ispossible(y, x):

        print('참', y, x)
        arr[y][x] = 1
        k += 1
        print(arr)
        dfs(y+1, x)
        arr[y][x] = 0
        k -= 1

        # 조건을 만족하지 못했을 때 그 전 노드로 올라가기
        else:
            print('부모로', arr)
            dfs(y-1, x)

N = int(input())  # 배열의 크기
arr = [[0] * N for _ in range(N)]

cnt = 0 # 개수 셀 것
# 1. 첫 행에서 배치하겠다

k = 0  # 노드 깊이
for x in range(N):
    dfs(0, x)

    print(cnt)



