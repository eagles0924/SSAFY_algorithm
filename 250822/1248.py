import sys
sys.stdin = open('1248.txt', 'r')


def dfs(node_num):
    global cnt
    if node_num == 0:       # v == 0???
        return
    cnt += 1
    dfs(L[node_num])
    dfs(R[node_num])
    return cnt

def dfs1(node_num, target, cnt):
    if node_num > target:
        return
    cnt += 1
    dfs1(1, L[node_num], cnt)
    dfs1(1, R[node_num], cnt)
    return cnt


T = int(input())
for tc in range(1, T+1):
    V, E, *target = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt, cnt1, cnt2 = 0, 0, 0
    L, R, P = [0] * (V + 1), [0] * (V + 1), [0] * (V + 1)
    for i in range(0, 2*E, 2):
        parent, child = arr[i], arr[i + 1]
        if L[parent] == 0:
            L[parent] = child
        else:
            R[parent] = child
        P[child] = parent
    # 두 target의 직속 parent를 비교해서 크면 한 단계 전의 parent로 올라가기
    # root 노드에서 target까지의 cnt를 계산하면 몇 번째 level인지 알 수 있음.
    # level이 큰 놈이 계속 올라오기
    t1, t2 = target
    cnt1 = dfs1(1, t1, cnt1)
    cnt2 = dfs1(1, t2, cnt2)
    while P[t1] != P[t2]:
        if cnt1 == cnt2 and P[t1] != P[t2]:
            t1 = P[t1]
        elif cnt1 > cnt2:
            t1 = P[t1]
        elif cnt1 < cnt2:
            t2 = P[t2]
        # if P[t1] > P[t2]:
        #     t1 = P[t1]
        # else:
        #     t2 = P[t2]
    same = P[t1]
    size = dfs(P[t1])
    print(f"#{tc} {same} {size}")