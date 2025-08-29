import sys
sys.stdin = open(r'C:\Users\SSAFY\vscode_psb\class_algo\250829\12917.txt', 'r')

"""
- 노드 번호는 정해져있음.
- 노드의 값을 받아 저장하는 것을 추가해야함.
- **N번 노드가 짝수인 경우 혼자 있기 때문에 부모 노드값은 이를 그대로 계승함.**
-  
"""
# 완전 이진 트리
# def c_binary(N):
#     for i in range(1, N+1):
#         if i > 1:
#             P[i] = i // 2
#         lc = 2 * i
#         rc = 2 * i + 1
#         if lc <= N:
#             L[i] = lc 
#         if rc <= N:
#             R[i] = rc
#     return P, L, R
    # E = N - 1
    # L = [0] * (N + 1)
    # R = [0] * (N + 1)
    # P = [0] * (N + 1)
    # V = [0] * (N + 1)
    # P, L, R = c_binary(N)
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    V = [0] * (N + 1)
# p: 부모 노드 번호, c: 자식 노드 번호, v: 노드에 주어질 값
    for _ in range(M):
        c, v = map(int, input().split())
        V[c] = v
        p = c // 2
        while p >= 1:
            V[p] += V[c]
            if p < 1:
                break
            else:
                p //= 2
    print(f"#{tc} {V[L]}")

# 옆으로 채우기

# for _ in range(M):


# 순회로 풀기

def post_order(n):
    if n > N:
        return
    left = post_order(2 * n)
    right = post_order(2 * n + 1)
    return left + right 

# 1 - 16
# 2 - 26
# 3 - 33
# 3 - 37
# 3 종료
# 2 - 29
# 2 종료
# 1 종료
##### out
# 29
