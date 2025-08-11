import sys
sys.stdin = open('12393.txt', 'r')

"""
1. brute force 사용
2. 멤버쉽 연산자 사용하지 말 것.
"""

T = int(input())
for tc in range(1, T+1):
    p = input()     # 패턴 문자열
    t = input()     # 전체 문자열
    i, j = 0 , 0
    m, n = len(p), len(t)
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j       # i 다시 원래 있던 인덱스로 초기화
            j = -1
        i += 1              # 이전에 탐색 시작했던 자리에서 한칸 오른쪽
        j += 1              # j는 인덱스 0부터 시작
    if j == m:
        print(f"#{tc}", 1)
    else:
        print(f"#{tc}", 0)

##### 오답노트
#  패턴 문자와 전체 문자.  p, t, i, j, m, n 너무 헷갈리는데 확실히 하고 갈 것.