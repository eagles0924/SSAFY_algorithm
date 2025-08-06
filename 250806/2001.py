import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    ### N은 배열 크기, M은 파리채 크기 ###
    arr = [list(map(int, input().split())) for _ in range(N)]
    best_fly = 0
    for i in range(N-M):
        for j in range(N-M):
            sum_fly = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    sum_fly += arr[r][c]
            if best_fly < sum_fly:
                best_fly = sum_fly
    print(f"#{tc} {best_fly}")