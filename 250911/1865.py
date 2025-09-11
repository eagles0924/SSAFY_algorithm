import sys
sys.stdin = open('1865.txt', 'r')

"""
- 확률 0이 포함되는 경우 무조건 넘겨야 함.
"""

def cal_best(clerk, cur_best, works):   # 받아오는 인자는 항상 갱신되어야 하기 때문에 global 쓰면 안됨.
    global N, best

    # backtracking
    if cur_best <= best:
        return
    # 종료 조건
    if clerk == N:
        best = cur_best
        return
    for work in range(N):
        # 0이 포함되면 계산하지 않고 pass
        if not percent[clerk][work]:
            continue
        if not works[work]:
            works[work] = 1
            cal_best(clerk + 1, cur_best * (percent[clerk][work] / 100), works)
            works[work] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    clerk, cur_best, best = 0, 1, -float('inf')
    works = [0] * N

    cal_best(clerk, cur_best, works)
    print(f"#{tc} {best*100}")