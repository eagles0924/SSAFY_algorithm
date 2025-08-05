'''
2
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
'''

def range_sum(arr, s, l):
    #  시작: s, 길이: l
    ret = 0
    for i in range(s, s + l):
        ret += arr[i]
    return ret


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    max_val = 0
    min_val = 1000000

    for s in range(N - M + 1):
        SUM = range_sum(lst, s, M)

        if max_val < SUM:
            max_val = SUM
        if min_val > SUM:
            min_val = SUM
    print(f'#{tc} {max_val - min_val}')