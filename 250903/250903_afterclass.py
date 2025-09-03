"""
이진수2
단순 이진 암호 코드
암호 코드 스캔
---------------------
러시아 국기 같은 깃발
쉬운 당근 포장
"""

arr = ['A', 'B', 'C', 'D']
N = len(arr)
R = 3
pick = [0] * R

def backtrack(k, start):
    if k == R:
        pass
    else:
        for i in range(start, N):
            pick[k] = arr[i]
            backtrack(k+1, i+1)

N = 5
arr = [i for i in range(N)]

# 2분할
for i in range(1, N):
    print(arr[:i], arr[i:])

for i in range(1, N-1):
    for j in range(i+1, N):
        print(arr[:i], arr[i:j], arr[j:])

# 2차 배열에서의 분할
arr = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(1, N):
        for r in range(i):
            for c in range(j):
                arr[r][c] = '-'
        for r in range(i):
            for c in range(j, N):
                arr[r][c] = '+'
        for r in range(i, N):
            for c in range(j):
                arr[r][c] = '+'
        for r in range(i, N):
            for c in range(j, N):
                arr[r][c] = '-'

