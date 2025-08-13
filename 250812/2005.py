import os
import sys
os.chdir(r'D:\vscode\SSAFY_algorithm\250812')
sys.stdin = open('2005.txt', 'r')

"""
재귀함수의 느낌이 난다.
"""
T = int(input())
def pascal(n):
    lst = [1]*n
    if n == 1 or n == 2:
        return lst
    else:
        lst_b = pascal(n-1)
        for i in range(1, n-1):
            lst[i] = lst_b[i-1] + lst_b[i]
        return lst
for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc}")
    for i in range(1, N+1):
        print(*pascal(i))

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     for i in range(N):





        # if i == 0 or i == 1:
        #     lst = [1]*(i+1)
        # else:
        #     lst = [1]*(i+1)
        #     lst[]