# SWEA1859

import sys
sys.stdin = open('1859.txt', 'r')


for tc in range(1, int(input())+1):
    # 매매일 수
    N = int(input())
    arr = list(map(int, input().split()))

    # 기준점
    mark = 0
    total = 0

    # 1. 뒤에서부터 큰 거 나올 때까지 탐색
    for i in range(N-1, -1, -1):
        if mark < arr[i]:
            mark = arr[i]

        # 1-1. 앞보다 뒤가 더 클 때
        else:
            total += mark - arr[i]

    print('#{} {}'.format(tc, total))