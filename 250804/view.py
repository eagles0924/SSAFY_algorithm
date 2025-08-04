T = 10

for test_case in range(1, T+1):
    N = int(input())
    height_list = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):         # 왼/오 양옆 0이므로 2 ~ N-3까지 순회
        h = height_list[i]
        h_max = 0
        near_list = [height_list[i+j] for j in range(-2,3) if j != 0]
        print(near_list)
        for near in near_list:
            if near > h_max:
                h_max = near
        if h_max >= h:
            continue
        diff = h - h_max
        cnt += diff
    print(f"#{test_case} {cnt}")




        # for j in range(1,3):
        #     if (h <= height_list[i+j]) or (h <= height_list[i-j]):
        #         break
        #     elif (h > height_list[i+j]) and (h > height_list[i-j]):
        #         if height_list[i+j] > h_max:
        #             h_max = height_list[i+j]
        #         if height_list[i-j] > h_max:
        #             h_max = height_list[i-j]
        # cnt += (h - h_max)



'''sys.stdin = open('input.txt')
T = int(input())
'''