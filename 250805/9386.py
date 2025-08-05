T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_order = input()
    # 숫자가 변하는 곳의 index 탐색
    cnt, max_cnt = 0, 0
    for idx, num in enumerate(num_order):       # 1로 끝나는 경우 max_cnt 갱신이 안됨.
        if num_order[idx] == '1':
            cnt += 1
        if num_order[idx] == '0':
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0
    if max_cnt < cnt:                           # 숫자 배열이 1로 끝나는 경우 좀 더 세련되게 끝낼 수는 없을까??
        max_cnt = cnt
    print(f"#{tc} {max_cnt}")