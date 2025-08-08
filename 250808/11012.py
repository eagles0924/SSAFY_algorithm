import sys
sys.stdin = open('11012.txt', 'r')

'''
1. 정사각형 하나씩 읽어들여 해당 범위에 포함된 값 합산하여 계산.
2. ** 합산한 범위들의 요소 값은 0으로 전환 ** >> 그래야 중복되어 계산하지 않는다.
3. 기본 프레임 벗어나는 경우는 try: except로 처리하기
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for _ in range(M):      # 하나씩
        r1, c1, length = map(int, input().split())
        for r in range(r1, r1+length):
            for c in range(c1, c1+length):
                # if로 제약조건 주기
                if (r < 0) or (r >= N) or (c < 0) or (c >= N):
                    break
                cnt += arr[r][c]
                arr[r][c] = 0
                # try:
                #     cnt += arr[r][c]
                #     arr[r][c] = 0       # 이미 한 번 확인한 자리는 중복되면 안되므로 0으로 변경
                # except:
                #     pass
    print(f"#{tc} {cnt}")

### try ~ except 비용이 많이 소요됨
### 예외처리하는 과정에서 꼬일 수가 있음.