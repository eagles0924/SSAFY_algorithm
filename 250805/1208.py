T = 10
for tc in range(1, T+1):
    N = int(input())        # 덤프 횟수 1 ~ 1000
    height_list = list(map(int, input().split()))       # 1 ~ 100
    h_min, h_min_idx, h_max, h_max_idx = 0, 0, 0, 0
    # counts_height = [0]*101
    for _ in range(N):
        for idx, height in enumerate(height_list):  # 상자 높이의 최댓값과 최솟값 (가장 앞의 index 기준) 반환
            if h_max < height:
                h_max = height
                h_max_idx = idx
            if h_min > height:
                h_min = height
                h_min_idx = idx
        height_list[h_max_idx] -= 1     # 해당 index(최고 높이)의 요소값 1 감소
        height_list[h_min_idx] += 1     # 해당 index(최저 높이)의 요소값 1 증가
        h_max -= 1; h_min += 1          
        diff = h_max - h_min
        if diff <= 1:
            break
    print(f"#{tc} {diff}")