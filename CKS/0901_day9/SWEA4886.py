# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('tournament.txt', 'r')

# 가위바위보
def winner(start, end):
    # 비기는 경우까지
    if (students[start - 1] - students[end - 1]) % 3 == 1 or (students[start - 1] - students[end - 1]) % 3 == 0:
        return start
    else:
        return end


def grouping(start, end):
    # 종료조건 설정
    if start == end:
        return start

    # 그룹 쪼개기
    first_group = grouping(start, (start + end) // 2)
    last_group = grouping((start + end) // 2 + 1, end)

    return winner(first_group, last_group)



T = int(input())    # test case

for tc in range(1, T+1):
    N = int(input())    # 인원수
    students = list(map(int, input().split()))

    start = 1
    end = N

    print('#{} {}'.format(tc, grouping(start, end)))
