import os
import sys

os.chdir(r"D:\vscode\SSAFY_algorithm\250806")
sys.stdin = open('23795.txt', 'r')

# 방향벡터 크기 무한대 (+제한 있어야 함.)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt, all = 0, 0     # 우주 괴물의 사정권 안의 지대 개수 및 전체 지대 개수 초기 선언
    # 괴물 위치의 x, y 좌표 받아오기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                all += 1
            if arr[r][c] == 2:
                x, y = r, c
    for way in range(4):
        for dis in range(1, N):
            nr = x + dr[way]*dis
            nc = y + dc[way]*dis
            # 범위 벗어나거나 1을 맞닥뜨렸을 때 멈춰야 하는 제약조건 추가.
            if (nr < 0) or (nr >= N) or (nc < 0) or (nc >= N) or (arr[nr][nc] == 1):
                break
            if arr[nr][nc] == 0:
                cnt += 1
    print(f"#{tc} {all - cnt}") 