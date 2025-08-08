import sys
from pprint import pprint
sys.stdin = open('16242.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 지그재그 순회
    arr = [[0]*10 for _ in range(10)]
    x, y, width, height = map(int, input().split())
    cnt = 1
    for r in range(x, x + height):
        for c in range(y, y + width):
            arr[r][c] = cnt
            cnt += 1
    print(f"#{tc}")
    pprint(arr)

'''
### 지그재그 순회
### 행 인덱스가 짝수일 때 > 정방향, 홀수일 때 > 역방향
cnt = 1
for r in range(N):
    if r % 2 == 0:
        for c in range(N):
            arr[r][c] = cnt
            cnt += 1
    else:
        for c in range(N-1, -1, -1):
            arr[r][c] = cnt
            cnt += 1
'''