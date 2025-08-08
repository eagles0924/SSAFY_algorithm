import sys
sys.stdin = open('12395.txt', 'r')

'''
1. str1에서 중복되는 문자 제거
2. str1_new 생성하여 해당 변수 안에 있는 문자에 대하여 str2 순회
'''

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    str1_new = list()
    for s1 in str1:
        if s1 not in str1_new:
            str1_new.append(s1)
    best_cnt = 0
    for s2 in str1_new:
        cnt = 0
        for target in str2:
            if s2 == target:
                cnt += 1
        if best_cnt < cnt:
            best_cnt = cnt
    print(f"#{tc} {best_cnt}")

###################### 딕셔너리 풀이법
