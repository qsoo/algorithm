def check(sp):

    # end point 방문했는지 확인
    while sp != ep:

        # start point visit
        visited[sp] = 1

        # 촌수 계산을 위해 route를 넣어줄 리스트 생성
        if not sp in result:
            result.append(sp)

        # 인접 행렬 중 방문 안 한 노드 찾기
        for i in adjacent_matrice[sp]:

                if not visited[i]:
                    visited[i] = 1
                    sp = i
                    break
        # pop
        else:
            result.pop()
            check(sp)

    return len(result)

N = int(input())    # 전체 사람 수(node)
sp, ep = map(int, input().split())  # 촌수 계산 대상
M = int(input())    # 부모 - 자식 관계의 수 (edge)

# 인접행렬 만들기
adjacent_matrice = [[] for _ in range(N + 1)]

for m in range(M):
    parent, child = map(int, input().split())
    adjacent_matrice[parent].append(child)
    adjacent_matrice[child].append(parent)

visited = [0] * N
# route
result = []
# 촌수 체크
count = check(sp)
print(count)