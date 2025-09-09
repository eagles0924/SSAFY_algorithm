import os
import sys
os.chdir(r'C:\vscode_psb\class_algo\250908')
sys.stdin = open('11804.txt', 'r')

# def move_container():
#     move = []
#     # 하나도 싣지 못하는 경우
#     if min(weights) > max(capacity):
#         return 0

#     while weights and capacity:
#         if capacity[-1] >= weights[-1]:
#             move.append(weights.pop())
#             capacity.pop()
#         else:
#             weights.pop()
#     return sum(move)
    
# QUEUE

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    weights.sort(); capacity.sort()
    move = []
    # 하나도 싣지 못하는 경우
    if min(weights) > max(capacity):
        ans = 0

    while weights and capacity:
        if capacity[-1] >= weights[-1]:
            move.append(weights.pop())
            capacity.pop()
        else:
            weights.pop()
    ans = sum(move)

    print(f'#{tc} {ans}')
