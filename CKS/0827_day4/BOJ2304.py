# https://www.acmicpc.net/problem/2304

def roof(height):
    # 나보다 크거나 같은 것을 만나기 전 인덱스까지는 나의 높이로
    max_height = height.index(max(height))

    # 좌측 시작
    benchmark, result = 0, 0
    for i in range(max_height):
        if height[i] > benchmark:
            benchmark = height[i]
        result += benchmark

    # 우측 시작
    benchmark = 0
    for i in range(len(height)-1, max_height, -1):
        if height[i] > benchmark:
            benchmark = height[i]

        result += benchmark

    result += height[max_height]
    return result

N = int(input())    # 기둥의 개수

location, height = [], []

# 위치와 높이를 두개의 리스트로 받겠다
for i in range(N):
    a, b = map(int, input().split())
    location.append(a)
    height.append(b)

# 위치좌표의 끝의 크기만큼 arr 생성
arr = [0 for _ in range(max(location) + 1)]

# 높이를 arr에 배치
for i in range(len(location)):
    arr[location[i]] = height[i]

print(roof(arr))
