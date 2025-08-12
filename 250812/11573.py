import sys
sys.stdin = open('11573.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    order = list(map(int, input().split()))

    s = []
    for num in order:
        if len(s) != 0 and num == 0:
            s.pop()
        else:
            s.append(num)
    ans = 0
    for num in s:
        ans += num
    print(f"#{tc} {ans}")