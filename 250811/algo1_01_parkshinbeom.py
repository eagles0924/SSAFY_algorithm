T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans_x, ans_y = -1, -1       # 정답의 x, y좌표의 초기값을 (-1,-1)로 하여 갱신되지 않을 경우(해당 좌표가 없을 경우) 그대로 출력되도록 한다.
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0             # *의 개수를 세는 cnt 변수를 선언하고 0을 할당해준다.
            for r in range(i, i+M):
                for c in range(j, j+M):
                    if arr[r][c] == '*':
                        cnt += 1            # *가 발견되면 cnt 1씩 증가
            if cnt == K:                    # 해당 부분 지역에서의 반복문을 다 돌고 cnt가 문제에서 원하는 개수이면 현재 좌표 저장
                ans_x, ans_y = i, j
                break
        if cnt == K:                        # 문제에서 조건을 만족하는 영역은 한 개 이하라고 했으므로 찾았다면 for문 종료
            break
    print(f"#{tc} {ans_x} {ans_y}")


# 아니면 함수를 만들어서 찾는 순간 return 하게끔 코드를 짜도 된다.
