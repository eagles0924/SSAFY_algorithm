from itertools import permutations
import os
os.chdir(r'D:\vscode\SSAFY_algorithm\250904')
import sys
sys.stdin = open('11803.txt', 'r')

# 1. 가지치기 없이 완전탐색

def backtrack(k, cur_cost, prev):
    global ans
    if ans <= cur_cost:     # 현재 값이 최솟값보다 커지는 순간 return
        return
    if k == N:
        cur_cost += G[prev][0]
        if ans > cur_cost:
            ans = cur_cost
        return
        # cost = 0
        # for i in range(1, N):
        #     cost += G[order[i-1]][order[i]]
        # cost += G[order[N-1]][0]
    else:
        for i in range(N):
            if visited[i]: continue
            visited[i] = 1
            backtrack(k + 1, cur_cost + G[prev][i], i)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # cases = permutations([i for i in range(1, N)], N-1)   # cases: 모든 경로
    visited = [0] * N
    G = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e10  # 우선 굉장히 큰 값 저장

    visited[0] = 1
    backtrack(1, 0, 0)
    print(ans)





    # min_sum = 1e5     # 배터리 사용량 최솟값
    # for case in permutations(range(1, N), N-1):
    #     cnt = arr[0][case[0]] + arr[case[-1]][0]   # 시점과 종점은 정해져있음. 소비량 시작과 끝 세팅
    #     # arr[0][case[0]] + arr[case[0]][case[1]] + arr[case[1]][case[2]] + ... + arr[case[N-3]][0]
    #     n = 0
    #     # while True:
    #     #     if n > len(case) - 2:
    #     #         break
    #     #     cnt += arr[case[n]][case[n+1]]
    #     #     n += 1
    #     for i in range(len(case)-1):
    #         cnt += arr[case[i]][case[i+1]]
    #     min_sum = min(min_sum, cnt)

    # print(f"#{tc} {min_sum}")
    # # 경로 경우의 수는 (n-2)!

