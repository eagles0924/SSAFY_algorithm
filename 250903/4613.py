# from itertools import combinations
# import sys
# sys.stdin = open('4613.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]
#
#     # 분할하여 문제 해결 (색이 3종류이기 때문에 분할 지점 2개 선정)
#     cuts = combinations([i for i in range(1, len(arr))], 2)
#     cnt_w, cnt_b, cnt_r = 0, 0, 0   # 흰, 파, 빨 칠해야 할 개수
#     for cut in cuts:
#         cut1, cut2 = cut


arr = 'WRWRW'
cnt = 0
for char in arr:
    if char != 'W':
        cnt += 1
print(cnt)

