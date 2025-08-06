import sys
sys.stdin = open(r'16268.txt', 'r')
# 델타 활용
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    best_cnt = 0    # 최다 꽃가루의 개수
    for r in range(N):
        for c in range(M):
            cnt = arr[r][c]  # 종이 꽃가루의 개수
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if (nr < 0) or (nr >= N) or (nc < 0) or (nc >= M):      ############### N,M 혼동 ###############
                    continue
                cnt += arr[nr][nc]
                if best_cnt < cnt:
                    best_cnt = cnt
    print(f"#{tc} {best_cnt}")
