import sys
sys.stdin = open('4408.txt', 'r')

"""
위: 출발, 아래: 도착 지점이라고 명시하자.
새로 들어온 출발 도착 지점을 기존의 출발 도착 지점과 비교하여야 한다.
위에서 출발하냐 아래에서 출발하냐는 영향을 주지 않는다.
시작점 ~ 끝점 선분 그어서 겹치는지만 확인하면 됨.
"""

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # start, end = [list(map(int, input().split())) for _ in range(N)]  # 시작과 끝점 받기
#     # uniquee = []
#     # for i in range(N):
#     #     start, end = map(int, input().split())
#     #     cnt = 0     # 서로 동시에 갈 수 없는 상황 개수
#     #     if cnt == 0:
#     #         cnt += 1; uniquee.append((start, end))
#     #         continue
#     #     for s, e in uniquee:
#     #         if
#     # cnt = 0
#     # route = dict()
#     # for i in range(N):
#     #     start, end = map(int, input().split())
#     #     if cnt == 0:
#     #         cnt += 1
#     #         route[start] = end
#     #         continue
#     #     min_start = min(route.keys())
#     #     max_end = max(route.values())
#     #     if max_end >= start:
#     #         route[start] = end
#     # print(len(route))
#     se = [list(map(int, input().split())) for _ in range(N)]
#     route = dict()
#     for i in range(200):
#         route[i] = 0
#     for start, end in se:
#         if start > end:
#             start, end = end, start
#         if start % 2 == 1:
#             for num in range(start, end+1, 2):
#                 idx = num // 2
#                 route[idx] += 1
#         else:
#             for num in range(start, end+1, 2):
#                 idx = num // 2
#                 route[idx] += 1
#             if end % 2 == 1:
#                 idx = end // 2
#                 route[idx] += 1
#
#     print(f'#{tc} {max(route.values())}')

"""
- 거꾸로 가는 경우 생각을 못함.
- 
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se = [list(map(int, input().split())) for _ in range(N)]
    route = dict()
    for i in range(1, 401):
        route[i] = 0
    for start, end in se:
        if start > end:
            start, end = end, start
        for num in range(start, end+1):
            route[num] += 1
    print(f'#{tc} {max(route.values())}')