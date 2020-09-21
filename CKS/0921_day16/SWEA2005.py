# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE

for tc in range(1, int(input())+1):

    N = int(input())

    # 파스칼 삼각형 넣을 배열 생성
    arr = [[0] * i for i in range(1, N+1)]

    # 1. 규칙에 맞게 파스칼 삼각형 생성
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            # 2. 처음과 끝은 1이다
            if x == 0 or x == (len(arr[y]) - 1):
                arr[y][x] = 1

            else:
                arr[y][x] += arr[y-1][x-1] + arr[y-1][x]

    print('#',tc, sep='')
    for i in arr:
        print(' '.join(map(str, i)))