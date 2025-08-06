import os
import sys

os.chdir(r"D:\vscode\SSAFY_algorithm\250806")
sys.stdin = open('12388.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    




'''
겹치는 건 네가지 경우가 있음.

'''