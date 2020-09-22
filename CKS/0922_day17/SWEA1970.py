import sys
sys.stdin = open('SWEA1970.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 1. 거스름돈으로 줄 수 있는 화폐종류와 개수 셀 리스트 생성
    type_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    type_cnt = [0] * 8

    # 거슬러 줄 총 잔액
    total = N

    # 2. 화폐종류를 탐색하면서 거스름돈을 줄여나간다
    for i in range(len(type_money)):
        # 종료 조건 설정
        if not total:
            break

        # 거스름돈으로 해당 화폐를 줄 수 있다면
        if total // type_money[i]:
            # 개수를 기록하고 남은 잔액을 갱신해준다
            type_cnt[i] = total // type_money[i]
            total = total % type_money[i]

    print('#{}'.format(tc))
    print(' '.join(map(str, type_cnt)))