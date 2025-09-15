import sys
sys.stdin = open('11898.txt', 'r')

"""
+1, -1, *2, -10을 가지고 몇 번을 사용하든지 N을 M으로 만드는 데에 드는 최소 연산 횟수
"""

# def calculator(num, a):
#     if num == 1:
#         a += 1
#     elif num == 2:
#         a -= 1
#     elif num == 3:
#         a *= 2
#     elif num == 4:
#         a -= 10
#     return a

# def dfs(cur_val, cnt, cal_type):
#     global N, M, min_cnt
#     if min_cnt <= cnt:
#         return
#     # 종료
#     if cur_val == M:
#         min_cnt = cnt
#         return
#
#     # 재귀
#     if cal_type == 1:
#         cur_val += 1
#         cnt += 1
#     elif cal_type == 2:
#         cur_val -= 1
#         cnt += 1
#     elif cal_type == 3:
#         cur_val *= 2
#         cnt += 1
#     elif cal_type == 4:
#         cur_val -= 10
#         cnt += 1
#
#     dfs(cur_val, cnt, 1)
#     dfs(cur_val, cnt, 2)
#     dfs(cur_val, cnt, 3)
#     dfs(cur_val, cnt, 4)

def bfs(start):


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0     # 연산 횟수

    min_cnt = float('inf')
    dfs(N, 0, 1)