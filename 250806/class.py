'''
arr1 = [[0]*4 for _ in range(3)]
arr1[1][1] = 10
arr1[2][1] = 15
print(arr1)
print(id(arr1[1][1]), id(arr1[2][1]))

# 얕은 복사???
arr2 = [[0]*4]*3
arr2[1][1] = 10
arr2[2][1] = 20
print(arr2)
print(id(arr2[1][1]), id(arr2[2][1]))

arr = [[0]*3 for _ in range(4)]
n, m = 3, 4
# 행 우선 순회, 열 우선 순회
for i in range(n):
    for j in range(m):
        arr[i][j]
# 열 우선 순회 굳이 돌릴 필요 없음.
for j in range(m):
    for i in range(n):
        arr[i][j]
# 지즈재그 순회 + (대각선 순회)
m-1-j
m-1-2j

for i in range(n):

# 부분 배열을 설정하여 순회 하기
# 부분 배열 크기 - M,

# 델타를 활용한 2차원 배열 탐색
### 인덱스 (행, 열) 기준으로 델타 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# pseudo code
# for k : 0 -> 3
#     ni <- i + di[k]
#     nj <- j + dj[k]

# **** 2차원 배열에서 4중 for문은 잦음 ****
arr = [[0]*20 for _ in range(20)]   # 20*20 배열로 가정
n, m = 20, 20
for i in range(len(arr)):
    for j in range(len(arr)):
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if (0 < ni < len(arr)) and (0 < nj < len(arr)):     # 유효성 검사
                arr[ni][nj]

for i in range(len(arr)):
    for j in range(len(arr)):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
# 추가: 각 방향으로 한칸이 아닌 k칸을 탐색하는 경우
max_v = None
for i in range(len(arr)):
    for j in range(len(arr)):
        s = arr[i][j]               # i, j(arr[i][j])를 중심으로
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]
            for c in range(1, k+1):
                ni, nj = i+di*c, j+dj*c
                if (0 <= ni < len(arr)) and (0 <= nj < len(arr)):
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s

# 전치 행렬 만들기

arr = [[1,2,3],[4,5,6],[7,8,9]]


# i,j의 크기에 따라 원소 접근


### 연습문제

arr = [[0]*5 for _ in range(5)]

for i in range(len(arr)):
    s += arr[i]
'''


######## 강사님 수업
N = 5
arr = [[0]*N for _ in range(N)]

### 행 우선 순회
cnt = 1
for r in range(N):
    for c in range(N):
        arr[r][c] = cnt
        cnt += 1
### 열 우선 순회
cnt = 1
for c in range(N):
    for r in range(N):
        arr[r][c] = cnt
        cnt += 1
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

### 행과 열의 크기가 다른 경우



### 전치 행렬
N = 6
arr = [[0]*N for _ in range(N)]

for r in range(N):
    arr[r][r] = 1

for r in range(N):
    arr[r][N-r-1] = 2

for r in range(N):
    for c in range(N):
        if r >= c:
            arr[r][c] = 1

for r in range(N):
    for c in range(r+1):    # r까지만 순회하면 위의 코드와 같다.
        arr[r][c] = 1

for r in range(N):
    for c in range(r+1, N):    # r까지만 순회하면 위의 코드와 같다.
        arr[r][c] = 1

# 부분 배열 순회

N = 7
arr = [[0]*N for _ in range(N)]

# 1. 좌상단 우하단 좌표를 안다.
# r1, c1 = 2, 1
# r2, c2 = 4, 5
# for r in range(r1, r2+1):
#     for c in range(c1, c2+1):
#         arr[r][c] = 1

# 2. 좌상단과 너비/높이를 안다.
r1, c1 = 2, 1
h, w = 3, 5

for r in range(r1, r1+h):
    for c in range(c1, c1+w):
        arr[r][c] = '*'


# 델타 이용한 탐색
N = 7
arr = [[0]*N for _ in range(N)]

# 1. 기준점 설정
r, c = 0, 6
arr[r][c] = '*'

# # 오른쪽
# arr[r+0][c+1] = 1
# # 아래
# arr[r+1][c+0] = 2
# # 왼쪽
# arr[r+0][c-1] = 3
# # 위
# arr[r-1][c+0] = 4

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # 좌표 생성 시, 반드시 유효한 값인지 검사
    if 1 <= nr < N and 0 <= nc < N:
        arr[nr][nc] = 'Y'


N = 7
arr = [[0]*N for _ in range(N)]

r, c = 3, 2
arr[r][c] = '*'

# for i in range(1, N):
#     nr = r + dr[0]*i
#     nc = c + dc[0]*i
#     if 0 <= nr < N and 0 <= nc < N:
#         arr[nr][nc] = 1

for direction in range(4):
    for i in range(1, 3):
        nr = r + dr[direction]*i
        nc = c + dc[direction]*i
        # if (0 <= nr < N) and (0 <= nc < N):
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            break
        arr[nr][nc] = 1

for row in arr:
    print(*row)

#######################
N, M = 5, 3
arr = [[0] * N for _ in range(N)]

for r1 in range(0, N-M+1):
    for c1 in range(0, N-M, 1):
        for r in range(r1, r1+M):
            for c in range(c1, c1+M):
                arr[r][c] = 1

########################
# 버스 리뷰

# while True:
#     for ~~:
#         break
#     else:
#         break   # for문은 이미 빠져나왔고 while을 빠져나오는 break
