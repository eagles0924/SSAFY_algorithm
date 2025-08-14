
















######## Backtraking




######## 강사님

# # 재귀함수 사용 시 유의할 것.
# import sys
# print(sys.getrecursionlimit())      # 재귀함수 호출 limit 확인
# sys.setrecursionlimit(10000)        # 재귀함수 호출 limit 변경
#
# # 재귀함수 호출 멈춤 조건은 내부의 변수가 아니라 외부의 변수 (매개변수)로 판단하도록 한다.
#
# def print_hello(i, n):
#     if i == n:
#         return
#     else:
#         print('hello', i)
#         print_hello(i+1, n)
#         print('hello', i)
#
# print_hello(0, 3)
#
# # stack을 사용하는 것과 같은 효과를 준다.
#
# def print_hello(i, n):
#     if i == n:
#         global cnt
#         cnt += 1
#         return
#     else:
#         print_hello(i+1, n)
#         print_hello(i+1, n)
# print_hello(0, 3)
#
# # cnt 값은 함수 호출 트리를 그려보기
# """
# 0,3                             다음과 같은 tree가 두 번 반복됨 (이진 트리)
#                                 debug로 실행시켜서 확인해보기
# 1,3             1,3             피보나치 다시 써보면서 확인하기
#
# 2,3     2,3     2,3     2,3
#
# 3,3 3,3 3,3 3,3 3,3 3,3 3,3 3,3
# """



######

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# G = [[0] * (V + 1) for _ in range(V + 1)]
G = [[] for _ in range(V + 1)] # 인접 리스트

for i in range(0, E*2, 2):
    # arr[i], arr[i+1]
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u)

for i in range(1, V + 1):
    print(i, '-->', G[i])

visited = [0] * (V + 1)


def DFS(v):  # v: 방문하는 정점
    visited[v] = 1; print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            DFS(w)
print()
DFS(1)



###### 백트래킹 --->>>> 을 잘하면 DP가 쉬워진다.
# 체계적으로 완전 탐색을 하려고 한다.
# 그래프 혹은 트리를 탐색하면서 최적해를 찾는다.
# 상태 공간 트리 -> 가상의 트리
# 답을 찾는 과정(결정 과정)을 트리로 표현

# 점화식 문제
# ㅣ, ㅁ, = 가 최소단위가 된다. (=가 왜 최소단위인 줄은 모르겠다)
# 문제에서 세로는 고정이고 가로길이가 늘어나기 때문에 ll은 최소단위가 되지 못함.
# 따라서 가로로 더 이상 쪼갤 수 없는 것이 최소 단위가 된다. ㅣ, ㅁ, =
# 이 세가지로 트리를 그려보기 (n=3)

def make_paper(n, paper):
    if n == 3:
        print(paper)
        return

    make_paper(n+1, paper + 'ㅣ')
    make_paper(n+2, paper + '=')
    make_paper(n+2, paper + 'ㅁ')

N = 3
cnt = 0

def make_paper_n(n, paper):
    if n > N:
        return
    if n == N:
        global cnt
        cnt += 1
        print(paper)
        return
    make_paper_n(n + 1, paper + 'ㅣ')
    make_paper_n(n + 2, paper + '=')
    make_paper_n(n + 2, paper + 'ㅁ')

def make_paper2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return make_paper2(n-1) + 2*make_paper2(n-2)