import os
import sys
os.chdir(r'C:\vscode_psb\class_algo\250908')
sys.stdin = open('11805.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: x[1])
    
    schedule = []
    schedule.append(time[0])
    for idx, (s, e) in enumerate(time):
        if idx >= len(schedule) and s >= schedule[-1][1]:
            schedule.append(time[idx])
    print(f'#{tc} {len(schedule)}')
