# # 16진수 > 2진수 변환
# hex_str = '68B4'
#
# for ch in hex_str:
#     print(f'{int(ch, 16):04b}', end=' ')
#
#
# '''
# 순열 N = 12 ~ 13, 부분집합 N = 20 넘어가면 터진다.
# DP로 접근할 것.
# > 분할정복, 특별한 자료구조 (Hasing, 구간 트리 등)
# > 안되면 탐욕(greedy) ㄱㄱ
#
# 최적화 문제 -> 완전 탐색
# - 전기카트 (TSP, Traveling Salesman Problem, 순회외판원문제)
# - 최소합
# - 최대상급
# '''
#
# # 암호코드 스캔
# pwd = {(3,2,1,1): 4, (1,2,3,1): 5, }
# # 등으로 생성
#
# T = int(input())
# N, M = map(int, input().split())
#
# line_set = set()
# for _ in range(N):
#     t = input().rstrip('0')
#     if t:
#         line_set.add(t)
# print(line_set)
# line = line_set.pop()
# idx = len(line) - 1
# codes = []
# for _ in range(8):
#     c1 = c2 = c3 = c4 = 0
#     # 1 카운팅
#     while line[idx] == '1':
#         c4 += 1; idx -= 1
#     # 0 카운팅
#     while line[idx] == '0':
#         c3 += 1; idx -= 1
#     # 1 카운팅
#     while line[idx] == '1':
#         c2 += 1; idx -= 1
#     # 0 카운팅
#     c1 = 7 - (c2 + c3 + c4)
#     idx -= c1
#     # print(pwd[(c1, c2, c3, c4)])
#     codes.append(pwd[(c1, c2, c3, c4)])
#
# b = sum(codes[0::2])
# a = sum(codes[1::2])
# # if (a * 3 + b)
#
#
#
# # 16진수 풀이
#
# line_set = set()
# for _ in range(N):
#     t = input().strip('0')
#     if t:
#         line_set.add(t)
# line = line_set.pop()
# bin_str = f'{int(line, 16):0>{len(line)*4}b}'.strip()
# codes = []
# cnt = 1
# for i in range(1, len(bin_str)):
#     if bin_str[i-1] == bin_str[i]:
#         cnt += 1
#     else:
#         codes.append(cnt)
#         cnt += 1
# # 마지막 카운팅 된 값 추가
# else:
#     codes.append(cnt)
#
# pwd_codes = []
# for i in range(0, len(codes), 4):
#     a, b, c = codes[i], codes[i + 1], codes[i + 2]
#
#     r = min(a, b, c)
#     pwd_codes.append(pwd[(a//r, b//r, c//r)])
#
#     # if lend


# 경로 찾기
N = 3
arr = [[0] * N for _ in range(N)]

cnt = 0
def gogo(r, c):
    global cnt
    if r >= N or c >= N:
        return
    arr[r][c] = 1   # 도달한 곳 경로 표시
    if r == N - 1 and c == N - 1:
        for line in arr:
            print(*line)
        print('-'*N)
        arr[r][c] = 0
        cnt += 1
        return
    gogo(r, c + 1)
    gogo(r + 1, c)
    # gogo(1,2), gogo(2,1), gogo(2,2) 같은 경우는 필요없이 연산을 여러 번 진행한다.

    arr[r][c] = 0

gogo(0,0)

# for line in arr:
#     print(*line)
print(cnt)


# backtracking

visited = [0] * N   # 방문 정보
order = [0] * N     # 방문 순서 기록
G = [list(map(int, input().split())) for _ in range(N)]
def backtrack(k, cur_cost):
    if k == N:
        print(order)
        cost = 0
        for i in range(1, N):
            cost += G[order[i-1]][order[i]]
        cost += G[order[N-1]][0]
        print(cost, cur_cost)
    else:
        for i in range(N):
            if visited[i]: continue
            visited[i] = 1
            order[k] = i    # i번 정점 방문
            backtrack(k + 1, cur_cost + G[order[k-1]][i])
            visited[i] = 0
backtrack(1)

visited = [0] * N
G = [list(map(int, input().split())) for _ in range(N)]
ans = 1e10  # 우선 굉장히 큰 값 저장

def backtrack(k, cur_cost, prev):
    global ans
    if ans <= cur_cost:     # 현재 값이 최솟값보다 커지는 순간 return
        return
    if k == N:
        cur_cost += G[prev][0]
        if ans > cur_cost:
            ans = cur_cost
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

# bit를 이용해 방문 정보 저장

N = 3
order = [0] * N
def backtracking(k, visited):
    if k == N:
        print(order)
    else:
        for i in range(N):
            if visited & (1 << i):
                continue
            order[k] = i
            backtrack(k + 1, visited | (1 << i))
