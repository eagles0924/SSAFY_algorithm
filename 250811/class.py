# p.37
N = int(input())
txt = [input() for _ in range(N)]

for r in range(1, N-1):
    for c in range(1, N-1):
        pass

# for else; cnt += 1 활용하기
# for 문이 다 돌면 else 문은 반드시 돈다.

##### 문자열 연산
def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[len(text)-i]:
            return False
    return True

##### Brute Force (pattern 파악하는 방법)
# i는 이전 시작 위치 + 1, j는 0으로 초기화
def brute_force(p, t):
    i, j = 0, 0
    m, n = len(p), len(t)
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j       #
            j = -1          # 밑에 j = 0으로 초기화를 해야하는데 밑에서 j += 1을 하기위해서는 j = -1로 설정해준다.
        i += 1
        j += 1
    if j == m:
        return i - m
    else:
        return -1

def brute_force2(p, t):
    m, n = len(p), len(t)
    cnt = 0
    for i in range(n-m+1):
        for j in range(m):
            if t[i+j] != p[j]:
                break
        else:
            return 1
    return -1

##### KMP algorithm
### lab.ssafy.com 에서 코드 확인
# LPS B형 준비 위해서 볼 것.
# Boyer-Moore algorithm - p.56

########## 강사님

p = ''
t = ''
n, m = len(t), len(p)

for i in range(n-m+1):
    for j in range(m):
        if p[j] != t[i + j]:
            break
    else:
        print(t[i:i+m])

##########################
n, m = len(t), len(p)
i, j = 0, 0

while j < m and i < n:
    if t[i] != p[j]:
        j = -1
        i = i - j
    i += 1
    j += 1
if j == m:
    print(t[i-j:i])