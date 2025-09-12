import sys
sys.stdin = open('11803.txt', 'r')

"""

"""

def find_route():
    global min_route


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))]

    min_route = 1e9

    find_r`oute()