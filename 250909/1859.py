import sys
sys.stdin = open('1859.txt', 'r')

"""
- 최댓값 위치 찾기.
    - 최댓값 나오기 전까지 buy, 최댓값 나오는 순간 sell
    - sell한 index까지는 고려할 필요 없음.
    - sell한 다음 index부터 다시 똑같이 반복
    - 만약 최댓값의 index가 0이라면 list.pop(0) 진행 후 다시 반복
"""

# def buy_sell():
#     global profit
#     if len(price) == 0:
#         return
#
#     while len(price):
#         max_price = max(price)
#         max_idx = price.index(max_price)
#         if max_idx == 0:
#             price.pop(0)
#         else:
#             for i in price[:max_idx]:
#                 profit += max_price - i
#             del price[:max_idx+1]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     price = list(map(int, input().split()))
#
#     profit = 0  # 얻을 수 있는 최대 이익
#     buy_sell()
#     print(f"#{tc} {profit}")

# 연산 시간 최적화 코드

def buy_sell():
    global profit
    if len(price) == 0:
        return

    start = 0
    while start < len(price):
        # max()와 index()를 한 번에 처리
        max_price = price[start]
        max_idx = start
        for i in range(start + 1, len(price)):
            if price[i] > max_price:
                max_price = price[i]
                max_idx = i

        if max_idx == start:
            start += 1
        else:
            # 구간합 계산
            for i in range(start, max_idx):
                profit += max_price - price[i]
            start = max_idx + 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    profit = 0  # 얻을 수 있는 최대 이익
    buy_sell()
    print(f"#{tc} {profit}")