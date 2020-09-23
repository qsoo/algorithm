# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE
import sys
sys.stdin = open('SWEA1208.txt', 'r')

for tc in range(1, 11):
    # 이동 제한 횟수
    total = int(input())
    # 상자들 배열
    li = list(map(int, input().split()))

    # 1. 정렬
    li.sort(reverse=True)

    # 2. 가장 높은 곳 => 두번째 높은 곳 될 때까지 가장 작은 곳에 주기
    for i in range(total):
        li[-1] += 1
        li[0] -= 1
        li.sort(reverse=True)

    result = max(li) - min(li)

    print('#{} {}'.format(tc, result))