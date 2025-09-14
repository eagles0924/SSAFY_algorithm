from itertools import permutations
import sys
sys.stdin = open('11803.txt', 'r')

"""
순열 문제
2 ~ N
반드시 1에서 출발 > 2 > 3 > ... > 1
1 > 3 > 4 > ... > 2 > 1
"""

# 재귀 쓰지 않고 풀면 memory error occur!!
# def find_route():
#     global min_route
#     way = [w for w in range(2, N + 1)]
#     for s in permutations(way):
#         cur_route = 0
#         for idx, p in enumerate(s):
#             # 첫 출발일 떄
#             if idx == 0:
#                 prev = 0
#                 cur_route += arr[prev][p-1]
#                 prev = p - 1
#             else:
#                 cur_route += arr[prev][p-1]
#                 prev = p - 1
#             if idx == len(s) - 1:
#                 cur_route += arr[prev][0]
#             if cur_route >= min_route:
#                 break
#         if min_route > cur_route:
#             min_route = cur_route

def min_route(start, prev, cur_route):
    global min_route
    # 백트래킹
    if min_route <= cur_route:
        return
    # 종료 조건
    if
    # 순회

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_route = 1e9
    find_route()
    print(min_route)
    print(sys.getsizeof(arr))
