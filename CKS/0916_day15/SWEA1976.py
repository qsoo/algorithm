# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE

T = int(input())

for tc in range(1, T+1):
    hour_1, minute_1, hour_2, minute_2 = map(int, input().split())

    # 1. 시간과 분을 각각 더한다

    new_hour = hour_1 + hour_2
    new_minute = minute_1 + minute_2

    # 2. 분이 60이 넘어가면 올림
    if new_minute > 60:
        new_hour += 1
        new_minute = new_minute - 60

    # 3. 시간은 1 ~ 12까지의 값을 가지므로 24시일 경우 주의해서 조건 주기
    if new_hour % 12:
        new_hour = new_hour % 12
    else:
        new_hour = 12
    print('#{} {} {}'.format(tc, new_hour, new_minute))
