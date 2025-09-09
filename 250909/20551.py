import sys
sys.stdin = open('20551.txt', 'r')

"""
a b c
a c b
b a c
b c a
"""
"""
- A, B, C개
- 순증가 해야함 (A < B < C)
- 각 상자에는 1개 이상의 사탕이 있어야 함.

- C 상자는 건들 필요 없음.
문제 설계
완전 탐색 후에 규칙을 발견하기. (규칙을 먼저 발견해서는 안됨)
1. 완전 탐색
2. 규칙 찾기

하나씩 줄여줘야 하는가?
한 번에 A, B, C 순서대로 되게끔 연산할 수는 없는가?
"""

T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())
    ans, cnt = 0, 0
    if b < 2 or c < 3:
        ans = -1
    elif a < b and b < c:
        ans = 0
    else:
        if b >= c:
            cnt = b - c + 1
            ans += cnt
            b = c - 1
        if a >= b:
            cnt = a - b + 1
            ans += cnt
            a = b - 1
    print(f"#{tc} {ans}")
