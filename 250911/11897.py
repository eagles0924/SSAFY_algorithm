# 항상 연산 수 먼저 대략 확인해보기
"""
- 열 중복 방지 (각 제품은 서로 다른 공장에서 생산해야 한다.
- 가지치기: 현재까지의 가격이 여태까지 구한 최솟값(best)보다 높아지면 return
- 상태 복원: 재귀 호출 후 공장 사용 상태를 원래대로 복원

"""
import sys
sys.stdin = open('11897.txt', 'r')


def find_cost(row, cur_sum, visit_factory):
    global N, min_sum, arr
    # backtracking
    if min_sum <= cur_sum:
        return
    # 종료 조건
    if row > N - 1:
        min_sum = cur_sum
        return
    for factory in range(N):
        # 제품(행)을 돌면서 해당 행에 대한 최솟값 찾기
        if not visit_factory[factory]:
            visit_factory[factory] = 1
            find_cost(row+1, cur_sum + arr[row][factory], visit_factory)
            visit_factory[factory] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]   # 해당 공장 및 제품 생산했는지 여부 확인
    visit_factory = [0] * N
    row, cur_sum, min_sum = -1, 0, float('inf')

    find_cost(0, 0, visit_factory)
    print(f"#{tc}", min_sum)
