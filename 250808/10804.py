import sys
sys.stdin = open('10804.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    before = input()
    after = list()
    for alpha in before:
        if alpha == 'b':
            after.append('d')
        elif alpha == 'd':
            after.append('b')
        elif alpha == 'p':
            after.append('q')
        elif alpha == 'q':
            after.append('p')
    ans = after[::-1]
    print(f"#{tc} {''.join(ans)}")