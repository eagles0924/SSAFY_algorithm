import sys
sys.stdin = open('12915.txt', 'r')


tree = [0, 4, 2, 6, 1, 3, 5]        # 완전 이진 트리

def inorder(v):
    pass
    inorder(v * 2)
    print(v, tree[v])   # v는 노드 번호, tree[v]는 저장된 번호
    # 부모의 왼쪽 노드에는 부모보다 작은 값, 오른쪽 노드에는 부모보다 큰 값.
    # 내가 찾으려는 값이 root node 보다 큰지 작은지를 확인한 후에 탐색할 파트를 찾으면 된다.
    inorder(v * 2 + 1)


for tc in range(1, T+1):
    N = int(input())
