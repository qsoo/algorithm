# https://www.acmicpc.net/problem/2477\

T = int(input())    # 1m^2에 자라는 참외의 개수

field = [int(input().split()[1]) for _ in range(6)]

# 가장 긴 변의 길이 추출
max_length_1= max(field)
idx1 = field.index(max_length_1)
# 양 옆의 인덱스에 접근해서 나머지 가장 긴 변 추출
if field[idx1 - 1] <= field[(idx1 + 1) % 6]:
    max_length_2 = field[(idx1 + 1) % 6]
    first = idx1
else:
    max_length_2 = field[idx1 - 1]
    first = idx1 - 1

# small Rectangle
small_1, small_2 = field[(first + 3) % 6], field[(first + 4) % 6]

print(((max_length_1 * max_length_2) - (small_1 * small_2)) * T)