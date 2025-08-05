# dictionary, hashing, 값의 범위가 작을 때 사용 가능. 음수는 안됨(shift 시켜서 양수화를 진행하든지).

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = input()
    counts = [0]*10
    len_card_list = 0
    for _ in card_list:
        len_card_list += 1
    for i in range(len_card_list):
        counts[int(card_list[i])] += 1
    max_idx, max_num = 0, counts[0]
    for idx, num in enumerate(counts):
        if max_num <= num:
            max_num = num
            max_idx = idx
    print(f"#{tc} {max_idx} {max_num}")