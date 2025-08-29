# 전위 / 중위 / 후위 순회 review

import sys
sys.stdin = open(r'C:\Users\SSAFY\vscode_psb\class_algo\250829\input.txt', 'r')

V = int(input())
E = V - 1
arr = list(map(int, input().split()))

left, right = [0]*(V+1), [0]*(V+1)
parents = [0]*(V+1)

for i in range(E):  # edge 정보를 담아야하므로 edge 수만큼 회문
    p, c = arr[i*2], arr[i*2+1]
    parents[c] = p
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

root = 1
for i in range(1, V+1):
    if parents[i] == 0:
        root = i
        break

def pre_order(T):
    if T > 0:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])
    
def in_order(T):
    if T > 0:
        in_order(left[T])
        print(T, end=' ')
        in_order(right[T])

def post_order(T):
    if T > 0:
        post_order(left[T])
        post_order(right[T])
        print(T, end=' ')

print(pre_order(1))
print(in_order(1))
print(post_order(1))

# list vs BST
# BST: 중위 순회하면 오름차순을 얻을 수 있다.

# 탐색할 값을 우선 root node와 비교한다.
# root 노드를 삭제할 때, 왼쪽 서브 트리의 가장 오른쪽 끝 자손.
# 힙은 이진탐색트리의 방법과는 무관. 형태만 같은 것.

### Max heap 구현

## 삽입

heap = [0]*100
last = 0

def enqueue(n):
    global last
    last += 1
    heap[last] = n

    child_num = last
    parent_num = child_num // 2     # 완전이진트리 자식 부모 비교 위해 번호 연산
    # 1. 부모가 있고, 2. 부모 < 자식 이면 키값 교환
    # while p:
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:      # 부모 존재하고, child가 parent보다 크면, (순서 중요)
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def dequeue():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                              # 비교 대상을 오른쪽 자식으로 지정
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c           # 자식을 새로운 부모로
            c = p * 2       # 왼쪽 자식 번호 계산
        else:
            break
    return tmp
enqueue(2)
enqueue(3)
enqueue(5)
enqueue(7)
enqueue(4)
enqueue(6)
print(heap)