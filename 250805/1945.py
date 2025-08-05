T = int(input())
for tc in range(1, T+1):
    N = int(input())
    exp_list = [0] * 5
    i = 0
    for insu in [2, 3, 5, 7, 11]:
        while N % insu == 0:
            N //= insu
            exp_list[i] += 1
        i += 1
    print(f"#{tc}", *exp_list)