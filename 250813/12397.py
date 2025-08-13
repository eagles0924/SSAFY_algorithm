import sys
sys.stdin = open('12397.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    if n%2 == 1:   # N이 10, 30, 50...인 경우
        pass

