import sys
sys.stdin = open('11802.txt', 'r')

def route(row, col, cnt):
    global min_cnt  # min_cnt는 누적 되어야하므로 arg로 설정하지 않고 global 인자로 설정
    if min_cnt <= cnt:
        return

    if row >= N or col >= N:
        return
    # 종료 기준 - (N-1, N-1)에 도달하면 탐색 종료
    if row == N-1 and col == N-1:
        cnt += arr[row][col]
        min_cnt = min(min_cnt, cnt)
        return

    route(row + 1, col, cnt + arr[row][col])
    route(row, col + 1, cnt + arr[row][col])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cnt = N * 10
    cnt = arr[0][0]     # 경로 지나는 곳 값의 합 초기 설정
    route(0, 0, 0)
    print(f'#{tc} {min_cnt}')




# 참고 코드
# DP
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    min_val = float('inf')
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = grid[0][0]
    # 첫 행과 첫 열 채우기
    for i in range(1, N):
        dp[0][i] = dp[0][i-1] + grid[0][i] # 위쪽에서만 올 수 있음.
        dp[i][0] = dp[i-1][0] + grid[i][0] # 왼쪽에서만 올 수 있음.
    # 나머지 테이블 채우기
    for r in range(1, N):
        for c in range(1, N):
            dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
    # finding_path(0, 0, grid[0][0])
    min_val = dp[N-1][N-1]
    print(f"#{test_case} {min_val}")

# BFS
from collections import deque

def bfs(r, c):
    basket = deque([(r, c)])

    while basket:
        p, q = basket.popleft()

        for i in range(4):
            np = p + dir_r[i]
            nq = q + dir_c[i]
            if 0 <= np < N and 0 <= nq < N and matrix[np][nq] + visited[p][q] < visited[np][nq]:
                visited[np][nq] = matrix[np][nq] + visited[p][q]

                if matrix[np][nq] == 0:
                    basket.appendleft((np, nq))
                else:
                    basket.append((np, nq))

    return visited[N - 1][N - 1]


T = int(input())
dir_r = [1, -1, 0, 0]
dir_c = [0, 0, 1, -1]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[2500] * N for _ in range(N)]
    visited[0][0] = matrix[0][0]

    result = bfs(0, 0)

    print(f"#{tc} {result}")
