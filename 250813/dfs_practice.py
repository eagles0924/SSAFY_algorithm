# import sys
# sys.stdin = open('')

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
arr = list(map(int, input().split()))

for i in range(0, 2*E, 2):
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u)

S = []  # 스택 생성
visited = [0]*(V+1)     # 방문 여부 생성

v = 1
visited[v] = 1          # 첫 index에 1 부여
print(v, end=' ')

while True:
    for w in G[v]:      # v번 vertex에 있는 값, 즉 v번 vertex와 연결된 vertex에 대해
        if not visited[w]:      # 방문한 적이 없다면,
            S.append(v)         # 현재 방문 경로에 추가
            visited[w] = 1      # 방문 이력에 방문 표시
            print(w, end=' ')
            v = w               # 다음 방문할 놈으로 v값 갱신
            break
    else:
        if not S:       # if True 일 때 실행이 되므로 stack이 빈 리스트일 때 break 실행 (이 경우 while 문을 종료시킴)
            break
        v = S.pop()     # stack에 아직 vertex가 남아있으면 pop 시키고 다시 for 문 돌입