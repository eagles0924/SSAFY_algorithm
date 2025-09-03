import sys
sys.stdin = open('1242.txt', 'r')

hexa = {''}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [input().strip() for _ in range(N)]

