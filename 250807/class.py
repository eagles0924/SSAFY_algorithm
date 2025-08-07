### 부분 집합 합 문제

bit = [0, 0, 0, 0]  # 문제에서 주어진 배열은 아님. 새로 생성하여 풀이 진행
for i in range(2):
    bit[0] = i
#
for i in [0, 1]:
    bit[0] = i
    for j in [0, 1]:
        bit[1] = j
# 이런 식으로 진행

arr = [2, 5, 4, 1]


def print_subset(arr, bit):
    for i in range(4):
        if bit[i]:  # bit[i]가 0이 아니면!!
            print(arr[i], end=' ')
    print(bit)


'''
bit와 byte의 관계
MSB, LSB(least significant bit)
'''

a = [0, 0, 1, 0]
b = [1, 0, 1, 1]
# a and b 비트 연산자 a | b

##### 비트 연산자 (p.30)

arr = [1,2,3]      # [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1 << n):   # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트 비교
        if i & (1 << j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=', ')  # j번 원소 출력
    print()
print()


### 순차 검색
ex = [4, 9, 11, 23, 2, 19, 17]
target = 2
ans = -1    # 못찾을 경우 대비하여 초기값을 없다는 의미인 -1로 설정
for i in range(len(ex)):
    if ex[i] == target:
        print('검색 성공!', i)
        ans = i
        break

# 순차 검색 대상이 **정렬되어 있지 않은** 경우



# 순차 검색 대상이 **정렬되어 있는** 경우
# 탐색 시간이 절반(??)으로 준다.

### 이진 검색
# 자료가 **정렬된 상태**에서 사용하는 방법
# 검색 목표 값과 중앙(기준)값을 비교하여 왼/오른쪽 탐색할 방향 설정
def binarySearch(a, N, key):    # a는 받아온 자료, N은 자료의 크기, key는 찾을 데이터
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2   # 중앙값 찾아서 middle에 설정
        if a[middle] == key:    # 마침 middle이면 검색 성공
            return middle
        elif a[middle] > key:   # 찾는 값이 중앙값보다 작으면
            end = middle - 1     # 왼쪽 구간 탐색
        else:
            end = middle + 1
    # 정ㅕㅕㅕㅕㅕ
    return -1

# or 재귀함수 이용

### 선택 정렬
# 버블 정렬과 헷갈리지 않기. 버블 정렬 - 이웃한 원소끼리 교환, 선택 정렬 - 최소값과 기준 위치의 값과 교환
def seletion_sort(a: list, N: int):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j     # 원소 교환까지 하진 않고, (현재까지) 최솟값의 자리를 저장하는 거까지만 작동한다.
        a[i], a[min_idx] = a[min_idx], a[i]     # 전역적 최솟값에 도달했을 때, 원소 스왑

# 우선 순위 1. 거품 정렬; 2. 선택 정렬; 3. 카운팅 정렬; 비교하여 학습.

### 셀렉션 알고리즘

# 작은 수 찾으면 오름차순, 큰 수 찾으면 내림차순으로 정렬해놓는 것이 좋다.

def selection(arr, key):
    pass
