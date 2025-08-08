import sys
sys.stdin = open('1221.txt', 'r')

'''
딕셔너리 생성하여 key: value로 각 숫자 단어(key)가 반복되는 개수(value)를 저장한 후 출력 
'''

T = int(input())
for tc in range(1, T+1):
    tc_num, N = input().split()
    numbers = input().split()
    order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dic = dict()
    for number in numbers:
        if number not in dic.keys():
            dic[number] = 1
        else:
            dic[number] += 1
    print(f"{tc_num}")
    for key in order:
        print(f"{(key+' ')*dic[key]}", end=' ')
    print()
