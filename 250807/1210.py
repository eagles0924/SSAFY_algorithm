import sys
sys.stdin = open('1210.txt', 'r')

# 1. 초기 i, j 설정은 2가 존재하는 지역으로 >> 거꾸로 타고 올라가야 출발점을 알 수 있다.
# 2. 좌, 우 탐색하여 1인 값이 없으면 상으로 이동 // 좌, 우 탐색 시 하나라도 1인 값이 있다면 해당 방향으로 이동
# 3. 좌/우로 진행할 때마다 0인지 1인지 탐색 후 이동하기. 0값 혹은 프레임을 벗어나면 해당 방향으로 이동 종료 후 상으로 이동
# 4. 상으로 이동 중 프레임을 벗어나면 종료 후 해당 좌표의 x좌표 반환

T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    end_r, end_c = 99, 0
    for c in range(100):
        if arr[end_r][c] == 2:
            end_c = c
    temp_r, temp_c = end_r, end_c
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    directions = [[-1, 0], [1, 0], [0, -1]]     # 좌 우 상
    while temp_r > 0:
        # 좌//우에 0이면 계속 상 방향으로 이동
        while (arr[temp_c-1][temp_r] == 0) and (arr[temp_c+1][temp_r] == 0):
            if temp_r == 0:
                break
            temp_r -= 1
        while arr[temp_c-1][temp_r] == 1:
            if (temp_c == 0) or (temp_c == 99):
                break
            temp_c -= 1
        while arr[temp_c+1][temp_r] == 1:
            if (temp_c == 0) or (temp_c == 99):
                break
            temp_c += 1
    print(f"#{tc} {temp_c}")

### 오답 노트
# 무한 루프 걸림. 좌우에 1이 있어도 위로 계속 이동하는 듯