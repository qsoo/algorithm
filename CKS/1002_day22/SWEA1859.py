# SWEA1859

import sys
sys.stdin = open('1859.txt', 'r')


def profit(li):
    global total
    if len(li) < 2:
        return
    idx = li.index(max(li))

    # 1. max까지의 이득
    total += (li[idx]*idx) - sum(li[:idx])

    # 2. 매매일 자르기
    li = li[(idx+1) :]

    if len(li) < 2:
        return
    profit(li)

for tc in range(1, int(input())+1):
    # 매매일 수
    N = int(input())
    arr = list(map(int, input().split()))

    total = 0
    profit(arr)

    print('#{} {}'.format(tc,total))