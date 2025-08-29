import sys
sys.stdin = open('12915.txt', 'r')

"""
즉 노드에 할당된 값은 중위 순회로 인한 노드 탐색 순서를 의미한다.
"""

def dfs(node_num):
    global order
    if node_num > N:            ### 어떨 때 등호이고 어떨 때 부등호인지????????????????????????????
        return
    dfs(2*node_num)
    # n번 노드의 값이 n_value라고 하자.
    # n_value
    # print(node_num, end=' ')
    order += 1
    orders[node_num] = order
    dfs(2*node_num + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    order, orders = 0, [0] * (N + 1)
    dfs(1)
    print(f"#{tc} {orders[1]} {orders[N//2]}")