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