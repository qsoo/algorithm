# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE
import sys
sys.stdin = open('SWEA1206.txt', 'r')

for tc in range(1, 11):
    # 건물 길이
    N = int(input())
    # 빌딩들
    li = list(map(int, input().split()))

    cnt = 0

    # 1. 탐색(비어있는 부분 제외하고 범위 설정)
    for i in range(2, N-2):
        # 2. 좌, 우 2칸씩 비교
        # 2-1. 비교 리스트 생성
        compare_li = li[i-2:i+3]
        compare_li.sort(reverse=True)
        # 2-2. 비교 리스트에서 i번째가 가장 크다면 조망권 확보 세대가 있다
        if compare_li[0] == li[i]:
           cnt += compare_li[0] - compare_li[1]

    print('#{} {}'.format(tc, cnt))
