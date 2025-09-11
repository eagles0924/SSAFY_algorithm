import sys
sys.stdin = open('1486.txt', 'r')
from itertools import combinations

def cal_min():
    global min_diff
    # backtracking - 1: 오름차순으로 정렬된 heights 처음부터 시작하므로 min_diff보다 커지면 바로 break
    # if min_diff < diff:
    #     return
    # Todo: backtracking - 2; 갱신되지 않은 채 더하는 명수가 늘면 바로 return
    # if
    for i in range(1, N+1):
        for combi in combinations(iter, 2):
            diff = 0
            for j in combi:
                diff += heights[j]
                if diff >= min_diff:
                    break
                min_diff = diff

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split())); heights.sort()
    iter = [i for i in range(N)]

    min_diff = float('inf')
    cal_min()
    print(min_diff)

# def recur(start, h):
#     global min_h
#
#     if min_h < B:
#         return
#
#     if h >= B:
#         min_h = min(min_h, h)
#         return
#
#     for i in range(start, len(arr)):
#         recur(i + 1, h + arr[i])
#
#
# T = int(input())
# for tc in range(1, 1 + T):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))
#     min_h = 100000
#     recur(0, 0)
#     print(f'#{tc} {min_h - B}')