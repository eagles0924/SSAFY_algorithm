import os
import sys
os.chdir(r'C:\vscode_psb\class_algo\250908')
sys.stdin = open('11806.txt', 'r')

"""
521290
395020

270250
872243
"""
# 연속인 숫자가 3이상
def run():
    while arr:

    pass


def triplet():
    pass




T = int(input())
for tc in range(1, T+1):
    p1, p2 = [], []
    # 한 번에 받지 말고 번갈아가면서 받아와야 누가 먼저 승리하는지 알 수 있음.
    arr = list(map(int, input().split()))
    # 그냥 한 번에 받아놓고, 마치 하나씩 받는 것처럼 pop으로 넣어주기
    while arr:
        # player 1에게 먼저 들어오므로 먼저 정렬 후 확인
        p1.append(arr.pop(0)); p1.sort()
        if len(p1) >=3:
            

        p2.append(arr.pop(0)); p2.sort()

        


