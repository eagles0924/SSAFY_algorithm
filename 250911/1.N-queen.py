# Backtracking

# PYTHON 1초에 3천만번 정도 연산

# 상태공간 트리 - 4Queens 문제
# 종료 조건: 4개 (행 고려)
# 가지의 수: 4개 (가지수 고려)

def recur(row):
    if row == N:    # N개의 행을 모두 탐색하면 종료
        return

    for col in range(N):
        # col 선택
        path.append(col)
        recur(row + 1)
        path.pop()  # 경로를 빠져나오면 그 경우는 제외해야지

    for col in range(N):
        # 가지치기: 한 번 선택한 열은 다시 못 고르도록 함.
        if visited[col]:
            continue
        # col 선택
        path.append(col)
        recur(row + 1)
        path.pop()  # 경로를 빠져나오면 그 경우는 제외해야지

    for col in range(N):
        # 가지치기: 한 번 선택한 열은 다시 못 고르도록 함.
        # 유망하지 않은 케이스 삭제 (세로, 대각선)
        if check(row, col) is False:
            pass
        # col 선택
        path.append(col)
        recur(row + 1)
        path.pop()  # 경로를 빠져나오면 그 경우는 제외해야지

def check(row, col):
    # 1. 같은 열에 놓은 적 있는가?
    for i in range(row):
        if visited[i][col]:     # y좌표 x좌표 순
            return False
    # 2. 좌상단 대각선에 놓은 적이 있는가? (\)
    i, j = row - 1, col - 1     # row, col 가까운 곳에서부터 시작
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1
    # 3. 우상단 대각선에 놓은 적이 있는가? (/)
    i, j = row - 1, col - 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False


    return True     # ????

N = 4
answer = 0
path = []; visited = [0] * N
recur(0)
