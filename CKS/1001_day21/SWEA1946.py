# SWEA1946

import sys
sys.stdin = open('1946.txt', 'r')

for tc in range(1, int(input())+1):
    # 알파벳과 숫자쌍의 개수
    N = int(input())
    compress = ''
    for _ in range(N):
        string, cnt = input().split()
        # 1. 각 개수별로 압축 풀어서 리스트에 저장하기
        compress += (string*int(cnt))

    # 2. slicing
    print('#{}'.format(tc))
    for i in range(0, len(compress), 10):
        print(compress[i:i+10])