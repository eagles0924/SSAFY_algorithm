import sys
sys.stdin = open(r'12388.txt', 'r')

'''
1. 빨강, 파랑이 각각 1, 2가 부여되므로, 보라색은 3으로 구분하여 나중에 arr[i][j]값이 3인 요소들의 개수만 더하기. 
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]       # 색칠하기 전 흰 도화지 준비
    for _ in range(N):  # 하나의 도형씩 받기
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1:
                    if arr[r][c] == 0:
                        arr[r][c] = 1
                    else:
                        arr[r][c] = 3
                elif color == 2:
                    if arr[r][c] == 0:
                        arr[r][c] = 2
                    else:
                        arr[r][c] = 3
    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                cnt += 1
    print(f"#{tc} {cnt}")
