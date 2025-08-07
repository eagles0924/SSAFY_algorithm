import sys
sys.stdin = open('12390.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    part, set_sum = map(int, input().split())   # part는 부분집합 원소의 개수, set_sum은 부분집합 원소의 합
    arr = [i for i in range(1, 13)]
    n = len(arr)
    for i in range(1<<n):
        cnt, summ = 0, 0
        idx = list()
        for j in range(n):
            if i & (1<<j):
                cnt += 1
                print(arr[j], end=' ')
        print()
    print()