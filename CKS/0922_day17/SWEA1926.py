
N = int(input())

arr = [str(i) for i in range(1, N+1)]

for i in range(len(arr)):
    str_num = arr[i]
    temp = 0
    if str_num.count('3') or str_num.count('6') or str_num.count('9'):
        temp += str_num.count('3')
        temp += str_num.count('6')
        temp += str_num.count('9')
        arr[i] = temp * '-'

print(' '.join(arr))