import sys
sys.stdin = open('12392.txt', 'r')

'''
1. 입력 받은 리스트 오름차순으로 정리 (selection sort 이용)
2. 새로운 리스트 생성하고, for문 이용하여  lst[N-1-i], lst[i] 순서대로 받아 저장
'''


def selection_sort(lst: list, n: int):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 선택 정렬 사용하여 오름차순으로 정렬
    order_list = selection_sort(numbers, N)
    answer = list()
    for i in range(N//2):
        if len(answer) >= 10:
            break
        answer.append(order_list[N-1-i])    # 최댓값 순서대로 append
        answer.append(order_list[i])        # 최솟값 순서대로 append
    print(f"#{tc}", *answer)
