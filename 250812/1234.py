import os
import sys
os.chdir(r'D:\vscode\SSAFY_algorithm\250812')
sys.stdin = open('1234.txt', 'r')

T = 10
for tc in range(1, T+1):
    N, raw = input().split()
    raw_list= list(raw)
    pw = []
    for raw in raw_list:
        if len(pw) == 0:
            pw.append(raw)
        elif len(pw) != 0 and raw == pw[-1]:
            pw.pop()
        else:
            pw.append(raw)
    print(f"#{tc}", ''.join(pw))

### stack top 이용해서 풀기
