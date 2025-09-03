def decimal_to_binary(n):
    binary_number = ''
    if n == 0:
        return 0
    while n > 0:
        remain = n % 2
        binary_number = str(remain) + binary_number
        n = n // 2

    return binary_number

print(decimal_to_binary(0))

def decimal_to_hexadecimal(n):
    hexadecimal_number = ''
    hexa_digits = '0123456789ABCDEF'
    if n == 0:
        return 0

    # 변화는 없고 조회만 필요할 때는 문자열이 편함
    # 변화가 필요한 경우에는 리스트 등
    while n > 0:
        remain = n % 16
        hexadecimal_number = hexa_digits[remain] + hexadecimal_number
        n = n // 16

    return hexadecimal_number

print(decimal_to_hexadecimal(15))
print(hex(30))

def binary_to_decimal(binary_str):
    decimal_number = 0
    for digit in reversed(binary_str):
        print(digit, end='')
    return  decimal_number

def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number

print(~112040)

secret_code = 1004
print(7070 ^ secret_code)
print(6258 ^ secret_code)

print('--------------------')
print(1 << 1, bin(1 << 1))
print(1 << 4, bin(1 << 4))


### 부분 집합

arr = [1, 2, 3, 4]
print(f'부분 집합의 수: {1 << len(arr)}')

# 전체 부분 집합 구하기
for i in range(1 << len(arr)):  # 부분집합 번호 반복
    for idx in range(len(arr)): # 각 원소들 모두 확인
        # i: 부분지합 번호 (각  자리 포함 여부)
        # (1 << idx): 0b1, 0b10,
        pass
    if i & (1 << idx):
        print(arr[idx], end='')
    print()

########
for i in range(1 << len(arr)):
    subset = []
    total = 0

    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]

    if total == 10:
        print(f'{subset}')

# p.70
WALK = 1 << 0
ATTACK = 1 << 1
JUMP = 1 << 2

