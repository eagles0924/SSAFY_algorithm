T = int(input())
for tc in range(1, T+1):
    tc_num = int(input())
    score_list = list(map(int, input().split()))
    # 카운팅 정렬
    counts = [0] * 101
    for i in range(len(score_list)):
        counts[score_list[i]] += 1      # 점수가 사실상 index의 역할을 하기 때문에 이런 식으로 작성.
    print(counts)
    max_cnt, max_idx = 0, 0
    for idx, cnt in enumerate(counts):
        if max_cnt <= cnt:
            max_cnt = cnt
            max_idx = idx
    print(f"#{tc} {max_idx}")
