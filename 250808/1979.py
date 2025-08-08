import sys
sys.stdin = open('1979.txt', 'r')

'''
- 칸이 남는 것도 안됨 무조건 K연타로 있는 자리만 가능 (K+1 연속 빈자리에 못 넣음)
- 방향은 가로 세로 상관없음.
1. 가로 / 세로 각각 순회하듯이 탐색하여 cnt = 3인 부분만 추출
2. 1 1 1 0 1과 같이 세 번 먼저 나왔는데 0 나와서 초기화되는 경우도 가능하기 때문에 추가.
>>> elif arr[r][c] == 0: 구문안에서 cnt 초기화하기 전에 ans += 1
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N):
        r_cnt, c_cnt = 0, 0
        for c in range(N):
            # 행 기준으로 순환
            if arr[r][c] == 1:
                r_cnt += 1
            elif arr[r][c] == 0:
                if r_cnt == K:        # 1 1 1 0 1과 같이 중간에 초기화되는 경우도 가능한 경우로 추가
                    ans += 1
                r_cnt = 0
            # 열 기준으로 순환
            if arr[c][r] == 1:
                c_cnt += 1
            elif arr[c][r] == 0:
                if c_cnt == K:
                    ans += 1
                c_cnt = 0
        if r_cnt == K:    # 0 0 1 1 1과 같이 모두 순회하고 나왔을 때 가능한 경우 추가
            ans += 1
        if c_cnt == K:    # 0 0 1 1 1과 같이 모두 순회하고 나왔을 때 가능한 경우 추가
            ans += 1
    print(f"#{tc} {ans}")