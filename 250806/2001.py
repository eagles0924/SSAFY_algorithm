import os
import sys
os.chdir(r"D:\vscode\SSAFY_algorithm\250806")
sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    ### N은 배열 크기, M은 파리채 크기 ###
    arr = [list(map(int, input().split())) for _ in range(N)]
    best_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):        # i, j 결정(초기 위치 설정)
            sum_fly = 0
            for r in range(i, i+M):
                for c in range(j, j+M):     # r, c 결정 (범위 내 파리 마리수 탐색)
                    sum_fly += arr[r][c]
            if best_fly < sum_fly:
                best_fly = sum_fly
    print(f"#{tc} {best_fly}")

##### 오답 노트
# range 범위 항상 잘 보기