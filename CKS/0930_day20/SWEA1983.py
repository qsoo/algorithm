# SWEA.1983 조교의 성적 매기기
import sys
sys.stdin = open('1983.txt', 'r')


for tc in range(1, int(input())+1):
    # 학생수, 타깃 학생번호
    N, K = map(int, input().split())
    # 1. 학생 점수 변환해서 받기
    result = [0] * N
    # 1-2. 점수 변수로 받기
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        mid, final, assign = map(int, input().split())
        result[i] = (mid * 0.35) + (final * 0.45) + (assign * 0.2)

    # 2. 타깃의 등수 확인(타깃은 0 idx부터 사용했기 때문에 -1 해줘야 함)
    cnt = 0
    for i in range(N):
        if result[K-1] < result[i]:
            cnt += 1
    target_grade = ''
    # 등급 부여
    target_grade = grade[int(cnt // (N / 10))]

    print('#{} {}'.format(tc, target_grade))


