# https://www.acmicpc.net/problem/2491
N = int(input())    # 수열의 길이
sequence = list(map(int, input().split()))  # 수열 들어있는 list



max_bigger, max_smaller = 1, 1   # 수열의 길이
total = 1

# bigger
for idx in range(N - 1):    # out of index 막자
    # out of index가 아닌 것 and 3개 더한게 2개 더한거 보다 클 때
    if sequence[idx] <= sequence[idx + 1]:
        total += 1
    else:
        total = 1    # reset

    # 제일 큰 값만 저장
    if max_bigger <= total:
        max_bigger = total

# smaller
total = 1   # reset
for idx in range(N - 1):    # out of index 막자
    if sequence[idx] >= sequence[idx + 1]:
        total += 1

    else:
        total = 1

    # 제일 큰 값만 저장
    if max_smaller <= total:
        max_smaller = total


# 둘 중에 큰 값 가져오기
if max_bigger <= max_smaller:
    print(max_smaller)

else:
    print(max_bigger)