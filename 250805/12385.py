T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    oil_station = list(map(int, input().split()))
    # station_all = [0] + oil_station + [N]   # 기점과 종점까지 포함하여 구성
    # # 1. 충전소 간격 때문에 불가능한 경우 (0 출력)
    # for i in range(M+1):
    #     if station_all[i+1] - station_all[i] > K:
    #         print(f"#{tc} {0}")
    #     break
    # 2. 가능한 경우
    ## 2-1. 충전소 간격 최대로 찾기 (i와 i+1 / i+2 / ... 간격이 K초과할 때까지 탐색
    stop, gap = 0, 0    # 멈출 횟수
    # road = [1] + [0]*(N-1) + [1]    # 기점과 종점까지 1부여 (1 사이 거리를 재기 위해)
    road = [0] * (N - 1)
    for i in range(M):
        road[oil_station[i]] = 1
    for station in road:
        if station == 0:
            gap += 1
            if gap == K:
                stop += 1
        elif station == 1:
            gap_save = gap
            gap += 1
            if gap == K:
                stop += 1