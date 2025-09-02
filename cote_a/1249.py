import sys
sys.stdin = open('1249.txt', 'r')

"""
10개 tc 30초 -> 1개 tc 3초 // 9000만번 연산

"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    int()