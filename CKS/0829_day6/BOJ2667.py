def dfs(y,x):
    # 1. stack 생성
    stack = [(y, x)]
    # 2. 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    global total
    num = 1 # 단지내 집의 수

    while stack:
        # 3. 탐색한다
        arr[y][x] = total
        # print(y, x, arr[y][x])
        num += 1
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]

            # 범위 설정
            if 0 <= new_y < N and 0 <= new_x < N and arr[new_y][new_x] == 1:
                # 탐색하지 않은 집들
                stack.append((new_y, new_x))
                # print(stack)
                y += dy[i]
                x += dx[i]
                break

        else:
            y, x = stack.pop()

    return int(num / 2)

N = int(input())    # 정사각형의 한 변의 길이


arr = [list(map(int, input())) for _ in range(N)]

total, cnt = 1, []  # 단지 수 + 1 / 단지내 집 수 리스트

# 1. 요소 하나씩 접근
for y in range(len(arr)):
    for x in range(len(arr[y])):
        # 2. 1인 곳 발견!
        if arr[y][x] == 1:
            total += 1
            cnt.append(dfs(y, x))

# 오름차순 정리 / sort - return none, 원본 변환 vs sorted - 정렬된 리스트 return
cnt.sort()

print(total - 1, '\n'.join(map(str, cnt)), sep='\n')
