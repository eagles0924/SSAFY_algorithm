import os
import sys
os.chdir(r'D:\vscode\SSAFY_algorithm\250804')
sys.stdin = open('1966.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     for i in range(N-1):
#         for j in range(i, N-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     print(f"#{tc}", *lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print(f"#{tc}", *lst)