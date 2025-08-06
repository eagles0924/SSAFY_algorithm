import os
import sys

os.chdir(r"D:\vscode\SSAFY_algorithm\250806")
sys.stdin = open('12712.txt', 'r')

# 델타 사용 + 범위 끝까지

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr1, dr2 = [0, 1, 0, -1], [1, 1, -1, -1]
    dc1, dc2 = [1, 0, -1, 0], [1, -1, -1, 1]
    best_fly = 0
    for r in range(N):
        for c in range(N):
            fly1, fly2 = arr[r][c], arr[r][c]
            for way in range(4):
                for dist in range(1, M):
                    nr1 = r + dr1[way]*dist
                    nc1 = c + dc1[way]*dist
                    if (nc1 < 0) or (nc1 >= N) or (nr1 < 0) or (nr1 >= N):
                        break
                    fly1 += arr[nr1][nc1]
            for way in range(4):
                for dist in range(1, M):
                    nr2 = r + dr2[way]*dist
                    nc2 = c + dc2[way]*dist
                    if (nc2 < 0) or (nc2 >= N) or (nr2 < 0) or (nr2 >= N):
                        break
                    fly2 += arr[nr2][nc2]
            best_fly = max(best_fly, fly1, fly2)
    print(f"#{tc} {best_fly}")

# 오답 노트
# max 사용할 때, best_fly도 넣어줘야 하는데 빼고 fly1, fly2만 진행함. 이러면 max_fly 경신이 안되고 각 case 별 최댓값만 추출됨. 