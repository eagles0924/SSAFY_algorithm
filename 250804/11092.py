T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ex_list = list(map(int, input().split()))
    max_num, min_num = ex_list[0], ex_list[0]
    max_idx, min_idx = 0, 0
    for idx, v in enumerate(ex_list):
        if v >= max_num:
            max_idx = idx
            max_num = v
        if v < min_num:
            min_idx = idx
            min_num = v
    if min_idx >= max_idx:
        diff = min_idx - max_idx
    else:
        diff = max_idx - min_idx
    print(f"#{tc} {diff}")

## max_num, min_num 안쓰이더라도 업데이트 해줘야지!!