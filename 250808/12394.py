import sys
from pprint import pprint
sys.stdin = open('12394.txt', 'r')

'''

'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word = [input() for _ in range(N)]
    for row in word:
        pprint(row)
    print('-------')