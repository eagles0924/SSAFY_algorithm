import os
import sys
os.chdir(r"D:\vscode\SSAFY_algorithm\250807")
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
            break
    temp_r, temp_c = end_r, end_c
    # dx = [1, 0, -1, 0]
    # dy = [0, 1, 0, -1]
    # directions = [[-1, 0], [1, 0], [0, -1]]     # 좌 우 상

    # 1. 좌나 우로 이동하다가 상으로 이동 시, 왔던 길 1이어서 무한 루프 걸리는 문제점 >> 왔던 길 0으로 바꾸어 해결
    # 2. 시작점이나 이동 중간에 0번 열이나 99번 열에 위치하여 arr[temp_r][temp+-r] 계산이 뜻대로 되지 않는 경우 >> 
    while temp_r > 0:
        # 좌//우에 0이면 계속 상 방향으로 이동
        ########## 위로 이동하는 경우
        if (temp_c != 0) and (temp_c != 99):
            while (arr[temp_r][temp_c-1] != 1) and (arr[temp_r][temp_c+1] != 1):
                if temp_r == 0:
                    break
                arr[temp_r][temp_c] = 0
                temp_r -= 1
        elif temp_c == 0:
            while arr[temp_r][temp_c+1] == 0:
                if temp_r == 0:
                    break
                arr[temp_r][temp_c] = 0
                temp_r -= 1
        elif temp_c == 99:
            while arr[temp_r][temp_c-1] == 0:
                if temp_r == 0:
                    break
                arr[temp_r][temp_c] = 0
                temp_r -= 1
        ############## 좌로 이동하는 경우 >> temp_c = 0인 경우 좌로 이동을 못하기에 처리해줘야 함.
        while arr[temp_r][temp_c-1] == 1:
            if temp_c == 0:
                break
            arr[temp_r][temp_c] = 0
            temp_c -= 1
        ############## 우로 이동하는 경우 >> 좌처럼 arr[-1]이 되는 게 아니라 arr[100]이 되어버리니까 에러문이 뜸.
        try:
            while arr[temp_r][temp_c+1] == 1:
                if temp_c == 99:
                    break
                arr[temp_r][temp_c] = 0
                temp_c += 1
        except:
            pass
    print(f"#{tc} {temp_c}")

### 오답 노트
# 무한 루프 걸림. 좌우에 1이 있어도 위로 계속 이동하는 듯
# 좌 혹은 우에서 오는 경우, 왔던 길이 1로 표기되어 있기 때문에 무한 루프에 걸림
# 따라서 왔던 길은 0으로 바꿔줄 예정.

### 두 번째 오답 노트
# 2가 맨 왼쪽 혹은 오른쪽에 있는 경우, 좌/우 검사 시 프레임에서 벗어나게 되므로 충족할 수 없다.