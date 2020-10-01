# SWEA1984
import sys
sys.stdin = open('1984.txt', 'r')

for tc in range(1, int(input())+1):
    # 판별할 숫자 리스트
    num_li = list(map(int, input().split()))
    # 1. 정렬(오름차순)
    num_li.sort()
    result = sum(num_li[1:9]) / 8

    # 2. 반올림 함수 구현
    if result >= int(result) + 0.5:
        result = int(result) + 1
    else:
        result = int(result)

    print('#{} {}'.format(tc, result))
