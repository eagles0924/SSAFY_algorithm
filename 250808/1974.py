import sys
sys.stdin = open('1974.txt', 'r')
# sys.stdout = open('1974_output.txt', 'w')

'''
- 행 / 열 / 3*3 각각 확인
- 1 ~ 9까지 모두 탐색해야 하므로 
'''

T = int(input())
checklist = [i for i in range(1,10)]
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 각 행과 열 모두 탐색
    for r in range(9):
        for c in range(9):
            pass
