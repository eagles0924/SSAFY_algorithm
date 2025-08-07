import sys
from pprint import pprint
sys.stdin = open('1954.txt', 'r')

#
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # 델타 사용; 막히거나, arr[r][c] != 0일 때
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]*N
    x, y = 0, 0
    cnt = 1
    arr[0][0] = 1
    for dx, dy in directions:
        for dist in range(1, N):
            nx = x + dx*dist
            ny = y + dy*dist
            # 정해진 N by N 프레임 벗어나거나, 0이 아닌 요소가 있는 곳으로 가면 위치 원상복구 후 방향 바꾸는 걸로
            if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= N) or (arr[nx][ny] != 0):
                nx = temp_x
                ny = temp_y
                break
            cnt += 1
            arr[nx][ny] = cnt
            temp_x, temp_y = nx, ny
        if N >= 2:
            x, y = nx, ny
        # arr 내부 모든 요소가 다 채워졌으면 for 문 종료
    print(f"#{tc}")
    for row in arr:
        print(*row)

### 오답노트
# temp_x, temp_y 저장해서 이전으로 돌아가는 것이 중요했음
# for문 말고 while 문 사용해서 풀이도 해보기