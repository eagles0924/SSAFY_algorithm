T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, 0, -1, 0]                  # 상하좌우를 둘러봐야 하기 때문에 이에 해당하는 델타 선언
    dc = [0, 1, 0, -1]
    ans = 0                             # 안전지대 장소 선언 및 0으로 초기화
    for r in range(1, N-1):             # 가장 자리 구역은 제외하기 때문에 (1,1)부터 (N-1, M-1)까지만 탐색하면 됨.
        for c in range(1, M-1):
            standard = arr[r][c]        # 안전지대인지 확인할 지역 (기준 지역)
            cnt = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]   # 크기가 1인 델타를 사용하므로 방향만 고려
                check = arr[nr][nc]             # 확인할 부분의 값을 check로 선언 (확인 지역)
                if standard <= check:           # 확인 지역이 기준 지역보다 크거나 같으면 안전지대 아니므로 for문 빠져나가기
                    break
                else:                           # 확인 지역이 기준 지역보다 작으면 cnt 1 추가
                    cnt += 1
            if cnt == 4:                        # cnt 값이 4이면 상하좌우 모두 기준 지역보다 값이 작으므로 안전지대 확정
                ans += 1                        # 안전지대 개수 1 증가
    print(f"#{tc} {ans}")
