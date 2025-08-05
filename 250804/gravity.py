# 맨 위 블럭만 고려해주면 된다. 그 아래 블럭의 떨어지는 값은 맨 위와 같거나 작을 수밖에 없음.
# 굳이 2차원 배열로 풀지 말 것.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    block_list = list(map(int, input().split()))
    max_v = 0
    for block in block_list:
        if block > max_v:
            max_v = block
    block_array = [[1]*i + [0]*(max_v-i) for i in block_list]
    max_row_cnt = 0
    for j in range(max_v - 1, -1, -1):
        max_col_cnt, cnt = 0, 0
        for i in range(N-1, -1, -1):
            if block_array[i][j] == 0:
                cnt += 1
            else:
                max_col_cnt = cnt
        if max_col_cnt > max_row_cnt:
            max_row_cnt = max_col_cnt
    print(f"#{test_case} {max_row_cnt}")

# 인덱스 값을 이요
# 하나의 쌓여있는 상자들의 낙차값
# 낙하 가능한 최대 거리 계산
# i = 0
# for i in range(N):
    # length = N - 1 - i
    # for j in range(i+1, N):
    #     if arr[i] <= arr[j]:
    #         length -= 1
    # if ans < length:
    #     ans = length