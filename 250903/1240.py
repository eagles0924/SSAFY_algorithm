import sys
sys.stdin = open('1240.txt', 'r')
# n = sys.stdin.readline()

pw = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
      '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [input() for _ in range(N)]
    # 암호 추출
    for line in info:
        if '1' in line:
            end = -line[::-1].index('1')
            start = end - 56
            code_raw = line[start:end]
            break
    # 십진수로 변경
    code = [pw[code_raw[7*i:7*(i+1)]] for i in range(8)]
    # 올바른 암호인지 판단
    check = 0
    for i in range(len(code)):
        if i % 2 == 0:
            check += 3 * code[i]
        else:
            check += code[i]
    if check % 10 != 0:
        print(f"#{tc}", 0)
    else:
        print(f"#{tc} {sum(code)}")