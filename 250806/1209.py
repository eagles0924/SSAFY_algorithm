import sys
sys.stdin = open(r'1209.txt', 'r')

T = 10
N = 100

# def check_best(best_sum, summ):
#     if best_sum < summ:
#         best_sum = summ
#     return best_sum

for tc in range(1, T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    summ_list = []
    best_sum = 0
    for r in range(N):
        summ = 0
        for c in range(N):
            summ += arr[r][c]
        if best_sum < summ:
            best_sum = summ
    for c in range(N):
        summ = 0
        for r in range(N):
            summ += arr[r][c]
        if best_sum < summ:
            best_sum = summ
    summ = 0
    for r in range(N):
        summ += arr[r][r]
    if best_sum < summ:
        best_sum = summ
    summ = 0
    for r in range(N):
        summ += arr[r][N-r-1]
    if best_sum < summ:
        best_sum = summ
    print(f"#{tc} {best_sum}")


# T = int(input())
# for tc in range(1, T+1):
#     matrix_list = list(map(int, input().strip().split()))
#     # 받아온 matrix 요소들 100*100으로 정리
#     SIZE = 100
#     # matrix = [[matrix_list[k*SIZE + i] for i in range(SIZE)] for k in range(SIZE)]
#     # arr = [[*map(int, input().split())] for _ in range(N)]
#     # 각 행, 열, 대각선의 합 구하기
#     summ_list = list()
#     best_sum = 0
#     # 행순환
#     for r in range(SIZE):
#         summ = 0
#         for c in range(SIZE):
#             summ += matrix[r][c]
#         if best_sum < summ:
#             best_sum = summ
#     # 열순환
#     for c in range(SIZE):
#         summ = 0
#         for r in range(SIZE):
#             summ += matrix[r][c]
#         if best_sum < summ:
#             best_sum = summ
#     # # 대각선
#     # for r in range(SIZE):
