import sys
sys.stdin = open('5656.txt', 'r')

def boom(x, y):    # n은 0 ~ W-1까지
    global W, H
    # 종료 조건
    if arr[x][y] == 0:
        return
    elif arr[x][y] == 1:
        arr[x][y] = 0
        return
    else:
        for i in range(1, arr[x][y]+1):
            print(point)
            point[(x, y)] = arr[x][y]
            boom(x-i, y)
            boom(x+i, y)
            boom(x, y-i)
            boom(x, y+i)
        arr[x][y] = 0   # 탐색 끝나고 0으로 변경
        return
    # Todo: 값 반환해서 1이면 arr[r][c]만 0으로 바꾸기
    # for r in range(H):
    #     if arr[r][n] == 1:
    #         arr[r][n] = 0
    #         break
    #     elif arr[r][n] >= 2:
    #         point[(r, n)] = arr[r][n]   # 2이상의 값을 가지는 좌표면 저장

# Todo: deepcopy 사용
def gravity():
    global W, H
    all = []
    for c in range(W):
        not_zero = []
        for r in range(H):
            if arr[r][c] != 0:
                not_zero.append(arr[r][c])
        not_zero += [0]*(H-len(not_zero))
        all.append(not_zero)
    all = list(map(list, zip(*all)))
    return all

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    point = dict()
    for _ in range(N):
        for c in range(W):
            for r in range(H):
                if arr[r][c] != 0:
                    boom(r, c)
            arr = gravity()
    cnt = 0
    for row in arr:
        for e in row:
            if e != 0:
                cnt += 1
    print(f'#{tc} {cnt}')



