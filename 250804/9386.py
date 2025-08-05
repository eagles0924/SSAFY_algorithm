T = int(input())
for tc in range(1, T+1):
    binary = input()
    cnt_max, cnt = 0, 0
    for num in binary:
        if num == 1:
            cnt += 1
        if cnt > cnt_max:
            cnt_max = cnt
    else:
        cnt = 0