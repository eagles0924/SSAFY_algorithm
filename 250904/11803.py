from itertools import permutations
import sys
sys.stdin = open('11803.txt', 'r')

# 1. 가지치기 없이 완전탐색

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # cases = permutations([i for i in range(1, N)], N-1)   # cases: 모든 경로

    min_sum = 1e5     # 배터리 사용량 최솟값
    for case in permutations(range(1, N), N-1):
        cnt = arr[0][case[0]] + arr[case[-1]][0]   # 시점과 종점은 정해져있음. 소비량 시작과 끝 세팅
        # arr[0][case[0]] + arr[case[0]][case[1]] + arr[case[1]][case[2]] + ... + arr[case[N-3]][0]
        n = 0
        # while True:
        #     if n > len(case) - 2:
        #         break
        #     cnt += arr[case[n]][case[n+1]]
        #     n += 1
        for i in range(len(case)-1):
            cnt += arr[case[i]][case[i+1]]
        min_sum = min(min_sum, cnt)

    print(f"#{tc} {min_sum}")
    # 경로 경우의 수는 (n-2)!

