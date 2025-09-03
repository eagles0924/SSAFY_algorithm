import sys
sys.stdin = open('12919.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    binary_number = ''
    s = 0.5
    while N > 0:
        if N - s >= 0:
            N -= s
            remain = 1
            s /= 2
            binary_number += str(remain)
        else:
            remain = 0
            s /= 2
            binary_number += str(remain)
        if len(binary_number) >= 13:
            break
    if len(binary_number) >= 13:
        print(f"#{tc}", 'overflow')
    else:
        print(f"#{tc} {binary_number}")

'''
소수점도 몫과 나머지를 계산할 수 있다는 것을 몰라 코드가 길어짐.
################# 참고 코드 ###################
T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    i = 1
    result = ''
    while N:
        result += str(int(N // (1/2**i)))
        N %= (1/2**i)
        i += 1
    if len(result) >= 13:
        result = 'overflow'
  
    print(f"#{tc} {result}")
'''