

T = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 1e10
def find_min(r, c, cur_sum):
    global ans
    
    ### 가지치기 추가
    ### cur_sum이 ans보다 커지면 더 탐색할 필요없이 바로 종료
    if ans <= cur_sum:
        return

    if r == N-1 and c == N-1:
        # 누적 합
        cur_sum += arr[r][c]
        # 위에서 비교했기 때문에 mind으로 비교할 필요 없다.
        # ans = min(ans, cur_sum)
        ans = cur_sum

        return
    
    if c + 1 < N:
        find_min(r, c+1, cur_sum + arr[r][c])
    
    if r + 1 < N:
        find_min(r+1, c, cur_sum + arr[r][c])

print(find_min((0, 0, 0)))

"""
memo[r][c-1] + arr[r][c]

memo[r-1][c] + arr[r][c]

둘 중에 min값을 채택.
"""

memo = [[-1]*N for _ in range(N)]
def find_mix2(r, c):
    
    if r == 0 and c == 0:
        return
    
    if memo[r][c] != -1:
        return memo[r][c]
    
    left, up  = 1e10, 1e010
    if c > 0:
        left = find_min(r, c-1)
    if r > 0:
        up = find_min(r-1, c)
    
    return min(left, up) + arr[r][c]

def find_min(r, c):
    for r in range(N):
        for c in range(N):
            if r == 0 and c == 0:
                memo[r][c] = arr[r][c]
            else:
                left = up = 1e10
                if c > 0:
                    left = memo[r][c-1]
                if r > 0:
                    up = memo[r-1][c]
                memo[r][c] = min(left, up) + arr[r][c]
        return memo[N-1][N-1]
print(find_min())
# for line in memo:

# 5188
