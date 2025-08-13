import sys
sys.stdin = open('12398.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]      # 왜 Vertex + 1인지 잘 생각해보기.
    arr = list(list(map(int, input().split())) for _ in range(E))
    start, end = map(int, input().split())

    for i in range(E):
        u, v = arr[i][0], arr[i][1]
        G[u].append(v)

    way = []
    visited = [0]*(V+1)
    v = start                   # vertex start부터 탐색이므로 start로 지정
    # print(v, end=' ')
    visited[v] = 1              # start는 방문했으므로 1주고 시작
    S = []

    while True:
        for w in G[v]:
            if not visited[w]:
                S.append(v)
                visited[w] = 1
                v = w
                # print(v, end=' ')
                way.append(v)
                break
        else:
            if not S:
                break
            v = S.pop()
    # print('------')
    if end in way:
        print(f"#{tc}", 1)
    else:
        print(f"#{tc}", 0)