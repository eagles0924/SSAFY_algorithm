test_case = int(input())

for i in range(test_case):
    N = int(input())
    ex_list = list(map(int, input().split()))
    min_num, max_num = ex_list[0], ex_list[0]
    for ex in ex_list:
        if ex < min_num:
            min_num = ex
        if ex > max_num:
            max_num = ex
    print(f"#{i+1} {max_num - min_num}")
