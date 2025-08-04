# 시작과 끝, 시작과 길이
test_case = int(input())

for t in range(1, test_case+1):
    N, M = map(int, input().split())
    ex_list = list(map(int, input().split()))
    for i in range(N-M+1):
        ex_sum = 0
        for j in range(M):
            ex_sum += ex_list[i+j]
            if i == 0:
                max_sum, min_sum = ex_sum, ex_sum
        if ex_sum > max_sum:
            max_sum = ex_sum
        if ex_sum < min_sum:
            min_sum = ex_sum
    print(f"#{t} {max_sum - min_sum}")