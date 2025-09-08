arr = [1, 2, 3, 4]

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[i], end='')

# 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크
def get_sub(tar):
    print('target =', tar, end=' / ')
    for i in range(len(arr)):
        if tar & 0x1:   # 가장 우측 비트를 체크 (16비트로 적은 건 암묵적 룰)
        # if tar & 1: # 1이기만 하면 된다.
            print(arr[i], end=' ')
        tar >>= 1

"""
순서 O > 순열
순서 X
 - 전체이면 부분집합
 - r개 고정이면 조합
"""