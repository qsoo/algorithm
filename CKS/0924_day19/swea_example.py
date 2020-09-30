import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # 학생 수, 문제 수
    N, M = map(int, input().split())
    sol_li = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    submit = 0


    for y in range(N):

        temp = [0] * M
        total = 0
        cnt = 0
        for x in range(M):
            if arr[y][x] == sol_li[x]:
                temp[x] = 1

        for i in range(len(temp)):
            if temp[i]:
                cnt += 1
                total += cnt

            else:
                cnt = 0

        result.append(total)

    submit = max(result) - min(result)

    print('#{} {}'.format(tc, submit))
