import sys
sys.stdin = open('12391.txt', 'r')

'''

'''


def binary(target, start, end):
    cnt = 0
    while start <= end:
        cnt += 1
        middle = int((start+end)/2)
        if middle == target:
            return cnt
        elif target < middle:
            end = middle
        elif target > middle:
            start = middle
    return cnt


T = int(input())
for tc in range(1, T+1):
    total_page, a, b = map(int, input().split())
    start, end = 1, total_page
    # A에 대해서 진행
    a_cnt, b_cnt = binary(a, start, end), binary(b, start, end)
    if a_cnt == b_cnt:
        print(f"#{tc}", 0)
    elif a_cnt < b_cnt:
        print(f"#{tc}", 'A')
    else:
        print(f"#{tc}", 'B')