import sys
sys.stdin = open('1952.txt', 'r')

def cal_min(cur_price, month):
    global min_price, d, m, m3, yr
    # 백트레킹
    # 현재 케이스의 가격이 최솟값보다 커질 때 종료
    print(month)
    if min_price <= cur_price:
        return
    # 월 이용일수 0일 때 (없을 때) 그냥 넘어가기

    # 종료 요건 (12월까지 모두 완료했다면)
    if month == 12:
        min_price = cur_price
        return

    # 계산 과정 - 1,2월/3월 이후
    if month <= 2:
        cur_price += min([plans[month] * d, m, m3, yr])
    else:
        cur_price += min([plans[month] * d, m, m3, yr])
    # 1월부터 순차적으로 계산
    # 1월: 일일이용권 vs 한달 이용권 vs 세달 이용권 vs 1년 이용권
    # 2월: 같음
    # 3월: 세달 이용권 vs 1,2월 최소값 + 일일/한달 이용권
    # 4월: 1월 최소 + 세달 이용권 vs 1~3월 최소 + 일일/한달 이용권
    # 5월: 1,2월 최소 + 세달 이용권 vs 1~4월 최소 + 일일/한달 이용권
    for i in range(month, 12):
        cal_min(cur_price, month + 1)

T = int(input())
for tc in range(1, T+1):
    d, m, m3, yr = map(int, input().split())
    plans = list(map(int, input().split()))

    min_price = float('inf')
    cal_min(0, 0)
    print(min_price)