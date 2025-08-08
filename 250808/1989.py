import sys
sys.stdin = open('1989.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     ans = 0
#     if word == word[::-1]:
#         ans = 1
#     print(f"#{tc} {ans}")

############### indexing 쓰지 않고 풀기

T = int(input())
for tc in range(1, T+1):
    before = input()
    after = list()
    for a in range(len(before)-1, -1, -1):
        after.append(before[a])
    result = ''.join(after)
    ans = 0
    if before == result:
        ans = 1
    print(f"#{tc} {ans}")