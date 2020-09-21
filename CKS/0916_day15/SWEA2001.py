# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE

import sys
sys.stdin = open('2001.txt', 'r')


def catchfly(y, x):
    global max_total
    # 각 기준점에서 잡은 파리수 임시 저장 변수 생성
    temp_total = 0
    for dy in range(M):
        for dx in range(M):
            temp_total += arr[y + dy][x + dx]

    # 2. 기존의 max_total보다 크다면 갱신 후 진행
    if temp_total > max_total:
        max_total = temp_total


T = int(input())

for tc in range(1, T+1):
    # N : 배열 차원, M : 파리채 크기
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 기준점을 선택해서 움직이자 => 파리채가 갈 수 있는 범위 정해짐
    # (N -M) index까지
    max_total = 0

    for y in range(N-M+1):
        for x in range(N-M+1):
            catchfly(y, x)

    print('#{} {}'.format(tc, max_total))