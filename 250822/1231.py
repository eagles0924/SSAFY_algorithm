import sys
sys.stdin = open('1231.txt', 'r')

def inorder(node_num):
    global order
    if node_num == 0:
        return
    inorder(L[node_num])
    order.append(node_num)
    inorder(R[node_num])
    return order



T = 10
for tc in range(1, T+1):
    N = int(input())
    L, R, P = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
    word = [0] * (N + 1)
    order = []
    for i in range(N):
        enter = input()
        if len(enter.split()) == 4:
            parent, letter, left_child, right_child = enter.split()
            parent, left_child, right_child = map(int, [parent, left_child, right_child])
            L[parent], R[parent], P[left_child], P[left_child] = left_child, right_child, parent, parent
            word[parent] = letter
        elif len(enter.split()) == 3:
            parent, letter, child = enter.split()
            parent, child = map(int, [parent, child])
            if L[parent] == 0:
                L[parent] = child
            else:
                R[parent] = child
            word[parent] = letter
            P[child] = parent
        else:
            parent, letter = enter.split()
            parent = int(parent)
            word[parent] = letter
    order = inorder(1)
    # print(*order)
    print(f"#{tc}", end=' ')
    for i in order:
        print(word[i], end='')
    print()

# 오답노트
# 계속 리스트 등 변수 초기화를 어디서 해야하는지 착각하고 있음.
# 완전 이진 탐색 문제라서 굳이 L, R, P 생성할 필요없음. 왜냐하면 노드가 다 설정되어 있기 때문에 자식 노드의 번호를 앎.
# 그리고 그냥 문자로 받아올 생각한 거부터가 패착. 리스트로 한 번에 받아오는 게 나음.

"""
def dfs(v):
    if v > N:
        return
    dfs(v*2)
    print(a_list[v],end='')
    dfs(v*2+1)
 
for tc in range(1,11):
    N = int(input())
    a_list = [0]
    for _ in range(N):
        b_list = list(input().split())
        a_list.append(b_list[1])
 
    print(f"#{tc}", end=' ')
    dfs(1)
    print()
"""