# SWEA1204
import sys
sys.stdin = open('1204.txt', 'r')

for tc in range(1, int(input())+1):
    input()
    score = list(map(int, input().split()))

    # 1. 점수별 빈도수 체크할 리스트 생성
    score_frequency = [0]*101

    for i in range(1000):
        score_frequency[score[i]] += 1

    most_frequency = 0
    cnt = 0
    # 2. 점수의 최빈수 찾기
    for i in range(101):
        if cnt <= score_frequency[i]:
            cnt = score_frequency[i]
            most_frequency = i

    # 2. 최빈수 확인
    print('#{} {}'.format(tc, most_frequency))