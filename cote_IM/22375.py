import os
import sys
os.chdir(r'D:\vscode\SSAFY_algorithm\cote_IM')
sys.stdin = open('22375.txt', 'r')

"""
같은 건 짝수번 조작, 다른 건 홀수번 조작
두 개의 스위치 리스트로 받고 마지막 인덱스부터 비교
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    cnt = 0     # 규칙이 바뀌는 횟수
    # for i in range(N-1):
    #     if ((s1[i] + s2[i])%2) != ((s1[i+1] + s2[i+1])%2):
    #         cnt += 1
    i = 0
    while i < N-1:
        if s1[i] == s2[i] and s1[i+1] != s2[i+1]:
            cnt += 1
        elif s1[i] != s2[i] and s1[i+1] == s2[i+1]:
            cnt += 1
        i += 1
    print(f"#{tc} {cnt}")


