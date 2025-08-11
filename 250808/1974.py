import os
import sys
os.chdir(r'D:\vscode\SSAFY_algorithm\250808')
sys.stdin = open('1974.txt', 'r')
# sys.stdout = open('1974_output.txt', 'w')

'''
- 행 / 열 / 3*3 각각 확인
- 1 ~ 9까지 모두 탐색해야 하므로 
'''

def selection_sort(lst: list):
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[j] = lst[j], lst[min_idx]
    return lst

T = int(input())
checklist = [i for i in range(1,10)]       # 1 ~ 9 모두 존재하는 checklist 생성
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 행 탐색
    for r in range(9):
        check = list()
        for element in arr[r]:
            check.append(element)
        check = selection_sort(check)
        if check == checklist:
