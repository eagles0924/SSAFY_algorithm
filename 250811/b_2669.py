# import sys
# sys.stdin = open('b_2527.txt' ,'r')

arr = [[0]*100 for _ in range(100)]             # 100*100 도화지 생성
for dot in range(1, 5):
    r1, c1, r2, c2 = map(int, input().split())
    width, height = r2 - r1, c2 - c1
    for r in range(r1, r1+width):
        for c in range(c1, c1+height):
            arr[r][c] = dot

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            cnt += 1
print(cnt)