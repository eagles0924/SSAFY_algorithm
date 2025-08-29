import sys
sys.stdin = open('12914.txt', 'r')

def node_cnt(node_num):
    global cnt
    if node_num == 0:
        return
    cnt += 1
    node_cnt(L[node_num])
    node_cnt(R[node_num])
    return cnt

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    for i in range(0, 2*E, 2):
        parent, child = arr[i], arr[i+1]
        if L[parent] == 0:
            L[parent] = child
        else:
            R[parent] = child
        P[child] = parent

    ans = node_cnt(N)
    print(f"#{tc} {ans}")

"""
왼쪽, 오른쪽 필요한 경우에는 문제 조건에서 명시를 해준다.
일반적으로 왼쪽 노드부터 채운다.
"""

        # 푸힣ㄱ힣ㄱ긱힉