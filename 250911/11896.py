import sys
sys.stdin = open('11896.txt', 'r')

def find_min_stop():
    global loc, cnt, min_cnt
    # 가지치기
    if cnt >= min_cnt:
        return
    # 종료 조건 (현재 위치가 stop_num 이상이 되면 종료)
    if loc >= stop_num - 1:
        min_cnt = cnt
        return
    # 경우의 수
    # max_loc = loc
    for i in range(1, stop[loc]+1):
        loc += i; cnt += 1
        find_min_stop()
        loc -= i; cnt -= 1

T = int(input())
for tc in range(1, T+1):
    stop = list(map(int, input().split())) + [0]
    stop_num = stop.pop(0)
    loc, cnt, min_cnt = 0, -1, float('inf')
    # cnt 기준으로 가지치기
    find_min_stop()
    print(f"#{tc} {min_cnt}")

# 재귀 안쓴 풀이

