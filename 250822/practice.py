# 전위 순회
#%%
'''
def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

# 중위 순회

def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)

# 후위 순회

def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)
'''
#%%

# 연습문제
'''
13 12        # 정점수 간선수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

import sys
sys.stdin = open('test.txt', 'r')

V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(0, E*2, 2):
    parent, child = arr[i], arr[i+1]
    if L[parent] == 0:          # L(왼쪽 노드)의 index parent에 아무것도 할당되어있지 않다면 child 할당
        L[parent] = child
    else:                       # L에 할당되어 있다면 R(오른쪽 노드)에 할당해주기
        R[parent] = child
    P[child] = parent           # 부모는 하나이므로 index child에 parent 할당
# index를 노드의 번호라고 했을 때, 해당 노드의 왼쪽 자식 (L), 오른쪽 자식 (R), 부모 노드 (P)를 저장해준다.

cnt = 0
def tree_traverse(v):
    global cnt
    if v == 0:      # 자식 노드가 없을 때
        return
    # 처음 진입했을 때
    tree_traverse(L[v])     # 왼쪽 자식노드
    # 왼쪽 자식에서 돌아온 후
    tree_traverse(R[v])      # 오른족 자식노드
    # 오른쪽에서 돌아온 후
    print(v, end=' ')
    cnt += 1

print(L)
print(R)
print(P)
tree_traverse(3); print(cnt)

