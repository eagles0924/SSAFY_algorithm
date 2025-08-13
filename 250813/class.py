####### 재귀 함수

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# def fibonacci(n):
#     if n == 0 or  n == 1:       # n < 2 아니면 n <= 1로 쓸 수 있다.
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# """
# 함수로 for 문을 짜주면 필요한 답이 나왔을 경우 바로 return 하면 필요없는 부분까지 돌지 않는다.
# def a():
#     for r in range ~~
#         for c in range ~~
#             for i in range() ~~
#                 for j in range() ~~
#                     return
# """
#
# ###### Memoization
# # 재귀함수는 불필요한 연산이 누적되므로, 연산이 누적되는 경우 메모리 낭비가 크다.
#
# def fibo1(n):
#     if n >= 2 and memo[n] == 0:
#         memo[n] fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
# cnt = 0
#
# memo = [0] * 11
# memo[0] = 0
# memo[1] = 1
# fibo1(10)

###### DP 동적 계획법 (A형까지는 괜찮지만 B형은 필수)

# def fibo2(n):
#     f = [0] * (n+1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n+1):
#         f[i] = f[i-1] + f[i-2]
#     return f[n]


###### DFS: 깊이 우선 탐색

"""
1. 지나간 곳을 저장하는 방식
2. 지나가지 않은 곳을 저장하는 방식??
"""
# visited, stack = [], []
# def DFS(v):
#     visited
#     while

# 방문시 True로 변경
# 방문 전이면 False

########### 강사님

"""
완전 탐색: 가능한 모든 후보를 조사
탐욕 기법
완전 탐색을 좀 더 효율적으로
    1. 백트래킹 - 탐색기반 및 가지치기
    2. 동적계획법 - 문제 간 관계 및 memoization

그래프 탐색 기법 - DFS, BFS
그래프는 vertex와 edge로 구성. 방향성 유무
그래프를 컴퓨터 메모리에 표현하는 방식
    1. 인접 행렬
    2. 인접 리스트 - 더 많이 사용
    
"""

###### DFS 연습문제3
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# G = [[0]*(V+1) for _ in range(V+1)]
G = [[] for _ in range(V+1)]     # Vertex 크기 + 1만큼 생성

for i in range(0, E*2, 2):
    # arr[i], arr[i+1]
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i, '-->', G[i])

# DFS를 위한 준비
# 그래프, 스택, visited(방문 정도) 3가지가 필요하다. (재귀 호출 시 스택은 필요없음)
S = []
visited = [0]*(V+1)
# 1. 시작 정점 v를 결정하여 방문한다.
v = 1   # 현재 위치한 정점
S.append(V)
visited[v] = 1
print(v, end=' ')

# 빈 스택이 아니면!
while S:    # //빈 스택이어야 하므로 S = []로 선언하지 않고 의미 없는 숫자 하나 넣어주기.//
    # 2. 정점 v에 인접한 정점 중에서 방문하지 않은 정점 w가 있으면,
    for w in G[v]:
        if not visited[w]:
            # v -----> w
            # 2.1) 정점 v를 스택에 push하고 정점 w를 방문한다.
            # 그리고 w를 v로 하여 다시 2를 반복한다.
            S.append(v)     # v를 stack에 push 한다는 것은 v -> w로 이동한다는 의미이다.
            visited[w] = 1  # 방문한 곳에 w 추가
            print(w, end=' ')
            v = w   # w를 현재 내 위치로 변경시킨다는 의미
            break   # //하나의 요소에 대해서만 진행하면 됨. -> 잘 이해 안감//
    else:
        # 방문하지 않은 정점이 없으면 탐색의 방향을 바꾸기 위해 stack을 pop 하여 받은 갖아 마지막 방문 vertex를 v로 하여 반복
        v = S.pop()     # 직전에 방문했던 요소 pop 해서 다시 v로 받기


#### 연습문제 3 구현
# 1. 방문한 곳을 stack에 추가하고
# 2. 방문 예정인 곳을 visited에 반영하고
# 3. v = w로 교체한다.


















