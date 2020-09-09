# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4&categoryId=AWcPjEuKAFgDFAU4&categoryType=CODE

import sys
sys.stdin = open('6190.txt', 'r')

def check_mono(num):
    tmp_str = str(num)
    for x in range(len(tmp_str) - 1):
        if tmp_str[x] > tmp_str[x+1]:
            return False

    return True


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 곱할 정수들 리스트
    integer_li = list(map(int, input().split()))

    # 곱의 결과값 저장할 임시 리스트와 최종 단조 증가 수 저장할 리스트 생성
    temp = 0

    max_num = -1


    # 1. 요소들의 곱 리스트 생성 => str
    for i in range(len(integer_li)):
        for j in range(i+1, len(integer_li)):
            temp = integer_li[i] * integer_li[j]
            if max_num < temp and check_mono(temp):
                max_num = temp


    print('#{} {}'.format(tc,max_num))



